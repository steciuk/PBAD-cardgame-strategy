import pytest

from simulation.deck.card import Card
from simulation.deck.deck import Deck
from simulation.game.simulator import SimulatorV2
from simulation.game.state.game_state import GameState
from simulation.game.state.player_state import PlayerState
from simulation.game_config.configs import GameConfig, RulesConfig
from simulation.game_config.enums import StrategyType
from simulation.game.player.strategies.greedy import GreedyStrategy

def test_greedy_base_scenario() -> None:
    PLAYER_ID = 0
    game_config: GameConfig = GameConfig()
    game_state: GameState = GameState(players_states=[
        PlayerState(0, Deck([Card('5H'), Card('5C'), Card('6C')]), StrategyType.GREEDY),
        PlayerState(1, Deck([Card('3H'), Card('3C'), Card('3S'), Card('2C'), Card('4S')]), StrategyType.OWN_FIRST)
    ], turn=0)
    simulator = SimulatorV2(game_config, game_state)
    game_state = simulator.turn()

    assert game_state.to_collect_by_id == (PLAYER_ID, {0: [Card('5H')], 1: [Card('3H')]})
    assert game_state.winner_id is None

    
    strategy = GreedyStrategy(PLAYER_ID, GameConfig())
    assert strategy.collect(game_state) == [Card('3H'), Card('5H')]

    game_state = simulator.turn([Card('3H'), Card('5H')])

    assert game_state.players_states[0].deck.cards == [Card('6C'), Card('3H'), Card('5H')]
    assert game_state.players_states[1].deck.cards == [Card('3S'), Card('2C'), Card('4S')]

def test_greedy_with_war() -> None:
    PLAYER_ID = 0
    game_config: GameConfig = GameConfig()
    game_state: GameState = GameState(players_states=[
        PlayerState(0, Deck([Card('KH'), Card('3C'), Card('9C'), Card('AC')]), StrategyType.GREEDY),
        PlayerState(1, Deck([Card('KH'), Card('5C'), Card('7C'), Card('KS'), Card('2C'), Card('4C'), Card('6C'), Card('8S'), Card('TC'), Card('QS')]), StrategyType.OWN_FIRST)
    ], turn=0)
    simulator = SimulatorV2(game_config, game_state)
    game_state = simulator.turn()

    assert game_state.to_collect_by_id == (PLAYER_ID, {0: [Card('KH'), Card('3C'), Card('9C')], 1: [Card('KH'), Card('5C'), Card('7C')]})
    assert game_state.winner_id is None
    
    strategy = GreedyStrategy(PLAYER_ID, GameConfig())
    assert strategy.collect(game_state) == [Card('3C'), Card('5C'), Card('7C'), Card('9C'), Card('KH'), Card('KH')]

    game_state = simulator.turn([Card('3C'), Card('5C'), Card('7C'), Card('9C'), Card('KH'), Card('KH')])

    assert game_state.players_states[0].deck.cards == [Card('3C'), Card('5C'), Card('7C'), Card('9C'), Card('KH'), Card('KH')]
    assert game_state.players_states[1].deck.cards == [Card('2C'), Card('4C'), Card('6C'), Card('8S'), Card('TC'), Card('QS')]