import pytest

from simulation.deck.card import Card
from simulation.game.state.player_state import PlayerState
from simulation.game_config.configs import GameConfig, PlayerConfig
from simulation.game_config.enums import CardsDistribution, DeckType, StrategyType
from simulation.utils.state.init_player_state import init_players_states


def test_init_players_state() -> None:
    game_config: GameConfig = GameConfig(
        cards_distribution=CardsDistribution.RANDOM,
        deck=DeckType.FULL,
        players=[
            PlayerConfig(StrategyType.OWN_FIRST),
            PlayerConfig(StrategyType.OWN_LAST),
        ]
    )
    player_states: list[PlayerState] = init_players_states(game_config)

    assert len(player_states) == 2
    assert player_states[0].id == 0
    assert player_states[1].id == 1
    assert player_states[0].strategy == StrategyType.OWN_FIRST
    assert player_states[1].strategy == StrategyType.OWN_LAST
    assert player_states[0].deck.size == 26
    assert player_states[1].deck.size == 26

    game_config = GameConfig(
        cards_distribution=CardsDistribution.RANDOM,
        deck=['2H', '3H', '4H'],
        players=[
            PlayerConfig(StrategyType.OWN_FIRST),
            PlayerConfig(StrategyType.OWN_LAST),
        ]
    )
    player_states = init_players_states(game_config)

    assert len(player_states) == 2
    assert player_states[0].deck.size == 1
    assert player_states[1].deck.size == 1

    game_config = GameConfig(
        cards_distribution=CardsDistribution.FIXED,
        players=[
            PlayerConfig(StrategyType.OWN_FIRST, cards=['2H', '3H', '4H']),
            PlayerConfig(StrategyType.OWN_LAST, cards=['5D']),
            PlayerConfig(StrategyType.OWN_LAST, DeckType.BLACK),
        ]
    )
    player_states = init_players_states(game_config)

    assert len(player_states) == 3
    assert player_states[0].deck.size == 3
    assert player_states[1].deck.size == 1
    assert player_states[0].deck.cards == [Card('2H'), Card('3H'), Card('4H')]
    assert player_states[1].deck.cards == [Card('5D')]

    game_config = GameConfig(
        cards_distribution=CardsDistribution.FIXED_RANDOM,
        players=[
            PlayerConfig(StrategyType.OWN_FIRST, cards=['2H', '3H', '4H']),
            PlayerConfig(StrategyType.OWN_LAST, cards=['5D', '6D']),
        ]
    )
    player_states = init_players_states(game_config)

    assert len(player_states) == 2
    assert player_states[0].deck.size == 3
    assert player_states[1].deck.size == 2
    for card in player_states[0].deck.cards:
        assert card in [Card('2H'), Card('3H'), Card('4H')]

    for card in player_states[1].deck.cards:
        assert card in [Card('5D'), Card('6D')]
