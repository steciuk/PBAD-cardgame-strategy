import pytest

from simulation.deck.card import Card
from simulation.deck.deck import Deck
from simulation.game.simulator import SimulatorV2
from simulation.game.state.game_state import GameState
from simulation.game.state.player_state import PlayerState
from simulation.game_config.configs import GameConfig, RulesConfig
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


def test_turn_no_players() -> None:
    game_config: GameConfig = GameConfig()
    game_state: GameState = GameState(players_states=[], turn=0)
    simulator: SimulatorV2 = SimulatorV2(game_config, game_state)

    game_state = simulator.turn()
    assert game_state.turn == 1
    assert game_state.players_states == []
    assert game_state.to_collect_by_id == (None, {})
    assert game_state.winner_id == -1


def test_turn_without_war() -> None:
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
    assert game_state.to_collect_by_id == (1, {0: [Card('2H')], 1: [Card('4H')]})
    assert game_state.winner_id is None

    game_state = simulator.turn([Card('4H'), Card('2H')])
    assert game_state.turn == 2
    assert game_state.players_states[0].deck.cards == []
    assert game_state.players_states[1].deck.cards == [Card('4H'), Card('2H')]
    assert game_state.to_collect_by_id == (1, {0: [Card('3C')], 1: [Card('5C')]})
    assert game_state.winner_id is None

    game_state = simulator.turn([Card('5C'), Card('3C')])
    assert game_state.turn == 3
    assert game_state.players_states[0].deck.cards == []
    assert game_state.players_states[1].deck.cards == [Card('4H'), Card('2H'), Card('5C'), Card('3C')]
    assert game_state.to_collect_by_id == (None, {})
    assert game_state.winner_id is 1


def test_turn_with_wars_no_draw() -> None:
    game_config: GameConfig = GameConfig(rules=RulesConfig(1))
    game_state: GameState = GameState(players_states=[
        PlayerState(0, Deck([Card('2D'), Card('3D'), Card('AC'), Card('6H')]), StrategyType.OWN_FIRST),
        PlayerState(1, Deck([Card('2H'), Card('3C'), Card('KC'), Card('5H')]), StrategyType.OWN_FIRST)
    ], turn=0)
    simulator = SimulatorV2(game_config, game_state)
    game_state = simulator.turn()

    assert game_state.turn == 1
    assert game_state.players_states[0].deck.cards == [Card('6H')]
    assert game_state.players_states[1].deck.cards == [Card('5H')]
    assert game_state.to_collect_by_id == (
        0, {0: [Card('2D'), Card('3D'), Card('AC')], 1: [Card('2H'), Card('3C'), Card('KC')]}
    )
    assert game_state.winner_id is None

    game_state = simulator.turn([Card('2D'), Card('3D'), Card('AC'), Card('2H'), Card('3C'), Card('KC')])
    assert game_state.turn == 2
    assert game_state.players_states[0].deck.cards == [
        Card('2D'), Card('3D'), Card('AC'), Card('2H'), Card('3C'), Card('KC')
    ]
    assert game_state.players_states[1].deck.cards == []
    assert game_state.to_collect_by_id == (
        0, {0: [Card('6H')], 1: [Card('5H')]}
    )
    assert game_state.winner_id is None

    game_state = simulator.turn([Card('6H'), Card('5H')])
    assert game_state.turn == 3
    assert game_state.players_states[0].deck.cards == [
        Card('2D'), Card('3D'), Card('AC'), Card('2H'), Card('3C'), Card('KC'), Card('6H'), Card('5H')
    ]
    assert game_state.players_states[1].deck.cards == []
    assert game_state.to_collect_by_id == (None, {})
    assert game_state.winner_id == 0


def test_turn_with_wars_simple_draw() -> None:
    game_config: GameConfig = GameConfig()
    game_state: GameState = GameState(players_states=[
        PlayerState(0, Deck([Card('2D'), Card('3D'), Card('AC'), Card('6H')]), StrategyType.OWN_FIRST),
        PlayerState(1, Deck([Card('2H'), Card('3C'), Card('AH'), Card('6D')]), StrategyType.OWN_FIRST)
    ], turn=0)
    simulator = SimulatorV2(game_config, game_state)
    game_state = simulator.turn()

    assert game_state.turn == 1
    assert game_state.players_states[0].deck.cards == []
    assert game_state.players_states[1].deck.cards == []
    assert game_state.to_collect_by_id == (None, {})
    assert game_state.winner_id == -1


def test_turn_with_wars_3_players() -> None:
    game_config: GameConfig = GameConfig(rules=RulesConfig(0))
    game_state: GameState = GameState(players_states=[
        PlayerState(0, Deck([Card('2D'), Card('4D'), Card('AC'), Card('7H'), Card('TH')]), StrategyType.OWN_FIRST),
        PlayerState(1, Deck([Card('2H'), Card('4C'), Card('KH'), Card('6D')]), StrategyType.OWN_FIRST),
        PlayerState(2, Deck([Card('2S'), Card('3S'), Card('5S'), Card('4C')]), StrategyType.OWN_FIRST),
    ], turn=0)
    simulator = SimulatorV2(game_config, game_state)
    game_state = simulator.turn()

    print(game_state)

    assert game_state.turn == 1
    assert game_state.players_states[0].deck.cards == [Card('7H'), Card('TH')]
    assert game_state.players_states[1].deck.cards == [Card('6D')]
    assert game_state.players_states[2].deck.cards == [Card('5S'), Card('4C')]
    assert game_state.to_collect_by_id == (
        0,
        {
            0: [Card('2D'), Card('4D'), Card('AC')],
            1: [Card('2H'), Card('4C'), Card('KH')],
            2: [Card('2S'), Card('3S')]
        }
    )
    assert game_state.winner_id is None

    game_state = simulator.turn([
        Card('2D'), Card('4D'), Card('AC'), Card('2H'), Card('4C'), Card('KH'), Card('2S'), Card('3S')
    ])

    assert game_state.turn == 2
    assert game_state.players_states[0].deck.cards == [
        Card('TH'), Card('2D'), Card('4D'), Card('AC'), Card('2H'),
        Card('4C'), Card('KH'), Card('2S'), Card('3S')
    ]
    assert game_state.players_states[1].deck.cards == []
    assert game_state.players_states[2].deck.cards == [Card('4C')]
    assert game_state.to_collect_by_id == (
        0, {0: [Card('7H')], 1: [Card('6D')], 2: [Card('5S')]}
    )
    assert game_state.winner_id is None

    game_state = simulator.turn([Card('7H'), Card('6D'), Card('5S')])

    assert game_state.turn == 3
    assert game_state.players_states[0].deck.cards == [
        Card('2D'), Card('4D'), Card('AC'), Card('2H'), Card('4C'),
        Card('KH'), Card('2S'), Card('3S'), Card('7H'), Card('6D'), Card('5S')
    ]
    assert game_state.players_states[1].deck.cards == []
    assert game_state.players_states[2].deck.cards == []
    assert game_state.to_collect_by_id == (0, {0: [Card('TH')], 2: [Card('4C')]})
    assert game_state.winner_id == None

    game_state = simulator.turn([Card('TH'), Card('4C')])

    assert game_state.turn == 4
    assert game_state.players_states[0].deck.cards == [
        Card('2D'), Card('4D'), Card('AC'), Card('2H'), Card('4C'), Card('KH'),
        Card('2S'), Card('3S'), Card('7H'), Card('6D'), Card('5S'), Card('TH'), Card('4C')
    ]
    assert game_state.players_states[1].deck.cards == []
    assert game_state.players_states[2].deck.cards == []
    assert game_state.to_collect_by_id == (None, {})
    assert game_state.winner_id == 0


def test_turn_1_player_with_cards() -> None:
    game_config: GameConfig = GameConfig(rules=RulesConfig(0))
    game_state: GameState = GameState(players_states=[
        PlayerState(0, Deck([]), StrategyType.OWN_FIRST),
        PlayerState(1, Deck([]), StrategyType.OWN_FIRST),
        PlayerState(2, Deck([Card('2S')]), StrategyType.OWN_FIRST),
    ], turn=0)
    simulator = SimulatorV2(game_config, game_state)
    game_state = simulator.turn()

    assert game_state.turn == 1
    assert game_state.players_states[0].deck.cards == []
    assert game_state.players_states[1].deck.cards == []
    assert game_state.players_states[2].deck.cards == [Card('2S')]
    assert game_state.to_collect_by_id == (None, {})
    assert game_state.winner_id == 2


def test_turn_3_players_with_no_cards() -> None:
    game_config: GameConfig = GameConfig(rules=RulesConfig(0))
    game_state: GameState = GameState(players_states=[
        PlayerState(0, Deck([]), StrategyType.OWN_FIRST),
        PlayerState(1, Deck([]), StrategyType.OWN_FIRST),
        PlayerState(2, Deck([]), StrategyType.OWN_FIRST),
    ], turn=0)
    simulator = SimulatorV2(game_config, game_state)
    game_state = simulator.turn()

    assert game_state.turn == 1
    assert game_state.players_states[0].deck.cards == []
    assert game_state.players_states[1].deck.cards == []
    assert game_state.players_states[2].deck.cards == []
    assert game_state.to_collect_by_id == (None, {})
    assert game_state.winner_id == -1


def test_turn_with_draw_war_between_2_players_3_player_without_cards() -> None:
    game_config: GameConfig = GameConfig(rules=RulesConfig(0))
    game_state: GameState = GameState(players_states=[
        PlayerState(0, Deck([Card('2H')]), StrategyType.OWN_FIRST),
        PlayerState(1, Deck([Card('2H')]), StrategyType.OWN_FIRST),
        PlayerState(2, Deck([]), StrategyType.OWN_FIRST),
    ], turn=0)
    simulator = SimulatorV2(game_config, game_state)
    game_state = simulator.turn()

    assert game_state.turn == 1
    assert game_state.players_states[0].deck.cards == []
    assert game_state.players_states[1].deck.cards == []
    assert game_state.players_states[2].deck.cards == []
    assert game_state.to_collect_by_id == (None, {})
    assert game_state.winner_id == -1


def test_turn_players_with_one_card_no_war() -> None:
    game_config: GameConfig = GameConfig(rules=RulesConfig(0))
    game_state: GameState = GameState(players_states=[
        PlayerState(0, Deck([Card('2H')]), StrategyType.OWN_FIRST),
        PlayerState(1, Deck([Card('2H')]), StrategyType.OWN_FIRST),
        PlayerState(2, Deck([Card('4H')]), StrategyType.OWN_FIRST),
    ], turn=0)
    simulator = SimulatorV2(game_config, game_state)
    game_state = simulator.turn()

    assert game_state.turn == 1
    assert game_state.players_states[0].deck.cards == []
    assert game_state.players_states[1].deck.cards == []
    assert game_state.players_states[2].deck.cards == []
    assert game_state.to_collect_by_id == (2, {0: [Card('2H')], 1: [Card('2H')], 2: [Card('4H')]})
    assert game_state.winner_id == None

    game_state = simulator.turn([Card('2H'), Card('2H'), Card('4H')])

    assert game_state.turn == 2
    assert game_state.players_states[0].deck.cards == []
    assert game_state.players_states[1].deck.cards == []
    assert game_state.players_states[2].deck.cards == [Card('2H'), Card('2H'), Card('4H')]
    assert game_state.to_collect_by_id == (None, {})
    assert game_state.winner_id == 2


def test_turn_unfinished_war_with_war_winner() -> None:
    game_config: GameConfig = GameConfig(rules=RulesConfig(0))
    game_state: GameState = GameState(players_states=[
        PlayerState(0, Deck([Card('3H')]), StrategyType.OWN_FIRST),
        PlayerState(1, Deck([Card('3D'), Card('5H')]), StrategyType.OWN_FIRST),
        PlayerState(2, Deck([Card('2H'), Card('4H')]), StrategyType.OWN_FIRST),
    ], turn=0)
    simulator = SimulatorV2(game_config, game_state)
    game_state = simulator.turn()

    assert game_state.turn == 1
    assert game_state.players_states[0].deck.cards == []
    assert game_state.players_states[1].deck.cards == [Card('5H')]
    assert game_state.players_states[2].deck.cards == [Card('4H')]
    assert game_state.to_collect_by_id == (1, {0: [Card('3H')], 1: [Card('3D')], 2: [Card('2H')]})
    assert game_state.winner_id == None

    game_state = simulator.turn([Card('3D'), Card('3H'), Card('2H')])

    assert game_state.turn == 2
    assert game_state.players_states[0].deck.cards == []
    assert game_state.players_states[1].deck.cards == [Card('3D'), Card('3H'), Card('2H')]
    assert game_state.players_states[2].deck.cards == []
    assert game_state.to_collect_by_id == (1, {1: [Card('5H')], 2: [Card('4H')]})
    assert game_state.winner_id == None

    game_state = simulator.turn([Card('5H'), Card('4H')])

    assert game_state.turn == 3
    assert game_state.players_states[0].deck.cards == []
    assert game_state.players_states[1].deck.cards == [
        Card('3D'), Card('3H'), Card('2H'), Card('5H'), Card('4H')
    ]
    assert game_state.players_states[2].deck.cards == []
    assert game_state.to_collect_by_id == (None, {})
    assert game_state.winner_id == 1


def test_turn_unfinished_war_with_no_war_winner() -> None:
    game_config: GameConfig = GameConfig(rules=RulesConfig(0))
    game_state: GameState = GameState(players_states=[
        PlayerState(0, Deck([Card('3H')]), StrategyType.OWN_FIRST),
        PlayerState(1, Deck([Card('3H')]), StrategyType.OWN_FIRST),
        PlayerState(2, Deck([Card('2H'), Card('5H')]), StrategyType.OWN_FIRST),
    ], turn=0)
    simulator = SimulatorV2(game_config, game_state)
    game_state = simulator.turn()

    assert game_state.turn == 1
    assert game_state.players_states[0].deck.cards == []
    assert game_state.players_states[1].deck.cards == []
    assert game_state.players_states[2].deck.cards == [Card('5H')]
    assert game_state.to_collect_by_id == (None, {})
    assert game_state.winner_id == 2


def test_turn_unfinished_war_with_game_winner() -> None:
    game_config: GameConfig = GameConfig(rules=RulesConfig(0))
    game_state: GameState = GameState(players_states=[
        PlayerState(0, Deck([Card('3H')]), StrategyType.OWN_FIRST),
        PlayerState(1, Deck([Card('3H'), Card('4H')]), StrategyType.OWN_FIRST),
        PlayerState(2, Deck([Card('2H')]), StrategyType.OWN_FIRST),
    ], turn=0)
    simulator = SimulatorV2(game_config, game_state)
    game_state = simulator.turn()

    assert game_state.turn == 1
    assert game_state.players_states[0].deck.cards == []
    assert game_state.players_states[1].deck.cards == [Card('4H')]
    assert game_state.players_states[2].deck.cards == []
    assert game_state.to_collect_by_id == (1, {0: [Card('3H')], 1: [Card('3H')], 2: [Card('2H')]})
    assert game_state.winner_id == None

    game_state = simulator.turn([Card('3H'), Card('3H'), Card('2H')])
    assert game_state.turn == 2
    assert game_state.players_states[0].deck.cards == []
    assert game_state.players_states[1].deck.cards == [Card('4H'), Card('3H'), Card('3H'), Card('2H')]
    assert game_state.players_states[2].deck.cards == []
    assert game_state.to_collect_by_id == (None, {})
    assert game_state.winner_id == 1


def test_turn_unfinished_war_with_no_war_winner_then_war() -> None:
    game_config: GameConfig = GameConfig(rules=RulesConfig(1))
    game_state: GameState = GameState(players_states=[
        PlayerState(0, Deck([Card('3H'), Card('4H')]), StrategyType.OWN_FIRST),
        PlayerState(1, Deck([Card('3S'), Card('4S')]), StrategyType.OWN_FIRST),
        PlayerState(2, Deck([Card('2D'), Card('5D'), Card('7D'), Card('8D')]), StrategyType.OWN_FIRST),
        PlayerState(3, Deck([Card('2S'), Card('5S'), Card('6S'), Card('7S')]), StrategyType.OWN_FIRST),
    ], turn=0)
    simulator = SimulatorV2(game_config, game_state)
    game_state = simulator.turn()

    assert game_state.turn == 1
    assert game_state.players_states[0].deck.cards == []
    assert game_state.players_states[1].deck.cards == []
    assert game_state.players_states[2].deck.cards == [Card('5D'), Card('7D'), Card('8D')]
    assert game_state.players_states[3].deck.cards == [Card('5S'), Card('6S'), Card('7S')]
    assert game_state.to_collect_by_id == (None, {})
    assert game_state.winner_id == None

    game_state = simulator.turn([])

    assert game_state.turn == 2
    assert game_state.players_states[0].deck.cards == []
    assert game_state.players_states[1].deck.cards == []
    assert game_state.players_states[2].deck.cards == []
    assert game_state.players_states[3].deck.cards == []
    assert game_state.to_collect_by_id == (
        2, {2: [Card('5D'), Card('7D'), Card('8D')], 3: [Card('5S'), Card('6S'), Card('7S')]}
    )

    game_state = simulator.turn([Card('5D'), Card('7D'), Card('8D'), Card('5S'), Card('6S'), Card('7S')])

    assert game_state.turn == 3
    assert game_state.players_states[0].deck.cards == []
    assert game_state.players_states[1].deck.cards == []
    assert game_state.players_states[2].deck.cards == [
        Card('5D'), Card('7D'), Card('8D'), Card('5S'), Card('6S'), Card('7S')
    ]
    assert game_state.players_states[3].deck.cards == []
    assert game_state.to_collect_by_id == (None, {})
    assert game_state.winner_id == 2


def test_simulator_returns_if_game_state_has_winner_id() -> None:
    game_config: GameConfig = GameConfig()
    game_state: GameState = GameState(players_states=[
        PlayerState(0, Deck([Card('2H'), Card('3C')]), StrategyType.OWN_FIRST),
        PlayerState(1, Deck([Card('4H'), Card('5C')]), StrategyType.OWN_FIRST)
    ], turn=0, winner_id=1)
    simulator = SimulatorV2(game_config, game_state)

    game_state = simulator.turn()
    assert game_state.turn == 0
    assert game_state.players_states[0].deck.cards == [Card('2H'), Card('3C')]
    assert game_state.players_states[1].deck.cards == [Card('4H'), Card('5C')]
    assert game_state.to_collect_by_id == (None, {})
    assert game_state.winner_id is 1


def test_simulator_raises_if_collection_order_needed_and_not_provided() -> None:
    game_config: GameConfig = GameConfig()
    game_state: GameState = GameState(players_states=[
        PlayerState(0, Deck([]), StrategyType.OWN_FIRST),
        PlayerState(1, Deck([]), StrategyType.OWN_FIRST)
    ],
        to_collect_by_id=(1, {0: [Card('2H')], 1: [Card('4H')]}),
        turn=0
    )
    simulator = SimulatorV2(game_config, game_state)

    with pytest.raises(ValueError) as err_info:
        simulator.turn()

    assert str(err_info.value) == 'Game state requires card collection, but no collection order was provided.'


def test_simulator_raises_if_cards_are_not_collected_properly() -> None:
    game_config: GameConfig = GameConfig()
    game_state: GameState = GameState(players_states=[
        PlayerState(0, Deck([]), StrategyType.OWN_FIRST),
        PlayerState(1, Deck([]), StrategyType.OWN_FIRST)
    ],
        to_collect_by_id=(1, {0: [Card('2H')], 1: [Card('4H')]}),
        turn=0
    )
    simulator = SimulatorV2(game_config, game_state)

    with pytest.raises(ValueError) as err_info:
        simulator.turn([Card('4H'), Card('3C')])

    assert str(err_info.value) == 'Invalid strategy. Cards were not collected properly.'

    with pytest.raises(ValueError) as err_info:
        simulator.turn([])

    assert str(err_info.value) == 'Invalid strategy. Cards were not collected properly.'

    with pytest.raises(ValueError) as err_info:
        simulator.turn([Card('2H'), Card('4H'), Card('AC')])

    assert str(err_info.value) == 'Invalid strategy. Cards were not collected properly.'

    with pytest.raises(ValueError) as err_info:
        simulator.turn([Card('2H'), Card('4H'), Card('4H')])

    assert str(err_info.value) == 'Invalid strategy. Cards were not collected properly.'


def test_simulator_raises_if_player_who_should_collect_cards_is_not_in_game_state() -> None:
    game_config: GameConfig = GameConfig()
    game_state: GameState = GameState(players_states=[
        PlayerState(0, Deck([]), StrategyType.OWN_FIRST),
        PlayerState(1, Deck([]), StrategyType.OWN_FIRST)
    ],
        to_collect_by_id=(2, {0: [Card('2H')], 1: [Card('4H')]}),
        turn=0
    )
    simulator = SimulatorV2(game_config, game_state)

    with pytest.raises(ValueError) as err_info:
        simulator.turn([Card('4H'), Card('2H')])

    assert str(err_info.value) == 'Player who should collect cards is not in the Game State.'
