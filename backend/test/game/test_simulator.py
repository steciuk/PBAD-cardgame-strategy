import pytest

from simulation.deck.card import Card
from simulation.deck.deck import Deck
from simulation.game.simulator import SimulatorV2
from simulation.game.state.game_state import GameState
from simulation.game.state.player_state import PlayerState
from simulation.game_config.configs import GameConfig
from simulation.game_config.enums import StrategyType


def test_game_state_copy_is_returned() -> None:
    game_config: GameConfig = GameConfig()
    game_state: GameState = GameState(
        players_states=[PlayerState(0, Deck([Card('2H'), Card('3C')]), StrategyType.OWN_FIRST)]
    )
    simulator: SimulatorV2 = SimulatorV2(game_config, game_state)

    assert simulator.game_state.players_states[0].id == 0
    game_state.players_states[0].id = 1
    assert simulator.game_state.players_states[0].id == 0
    new_game_state: GameState = simulator.turn()
    assert new_game_state.players_states[0].id == 0
    new_game_state.players_states[0].id = 2
    assert simulator.game_state.players_states[0].id == 0


def test_no_players() -> None:
    game_config: GameConfig = GameConfig()
    game_state: GameState = GameState(players_states=[], turn=0)
    simulator: SimulatorV2 = SimulatorV2(game_config, game_state)

    game_state = simulator.turn()
    assert game_state.turn == 1
    assert game_state.players_states == []
    assert game_state.to_collect is None
    assert game_state.winner_id == -1


def test_collect_without_war() -> None:
    game_config: GameConfig = GameConfig()
    game_state: GameState = GameState(players_states=[
        PlayerState(0, Deck([Card('2H'), Card('3C')]), StrategyType.OWN_FIRST),
        PlayerState(1, Deck([Card('4H'), Card('5C')]), StrategyType.OWN_FIRST)
    ], turn=0)
    simulator = SimulatorV2(game_config, game_state)
    game_state = simulator.turn()

    assert game_state.turn == 1
    assert game_state.players_states[0].deck.cards == [Card('3C')]
    assert game_state.players_states[1].deck.cards == [Card('5C')]
    assert game_state.to_collect == (1, {0: [Card('2H')], 1: [Card('4H')]})
    assert game_state.winner_id is None

    with pytest.raises(ValueError) as err_info:
        simulator.turn()

    assert str(err_info.value) == 'Game state requires card collection, but no collection order was provided.'

    game_state = simulator.turn([Card('4H'), Card('2H')])
    assert game_state.turn == 2
    assert game_state.players_states[0].deck.cards == []
    assert game_state.players_states[1].deck.cards == [Card('4H'), Card('2H')]
    assert game_state.to_collect == (1, {0: [Card('3C')], 1: [Card('5C')]})
    assert game_state.winner_id is None

    game_state = simulator.turn([Card('5C'), Card('3C')])
    assert game_state.turn == 3
    assert game_state.players_states[0].deck.cards == []
    assert game_state.players_states[1].deck.cards == [Card('4H'), Card('2H'), Card('5C'), Card('3C')]
    assert game_state.to_collect == None
    assert game_state.winner_id is 1
