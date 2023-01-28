import pytest

from simulation.game_config.configs import GameConfig, PlayerConfig
from simulation.game_config.enums import CardsDistribution, StrategyType


def test_num_players() -> None:
    config1 = GameConfig(players=[
        PlayerConfig(StrategyType.OWN_FIRST, None),
        PlayerConfig(StrategyType.OWN_FIRST, None),
        PlayerConfig(StrategyType.OWN_FIRST, None),
    ])
    assert len(config1.players) == 3

    with pytest.raises(ValueError) as err_info:
        GameConfig(players=[PlayerConfig(StrategyType.OWN_FIRST, None)])

    assert str(err_info.value) == 'At least 2 players are required.'


def test_cards_distribution_fixed() -> None:
    config1 = GameConfig(
        cards_distribution=CardsDistribution.FIXED,
        players=[
            PlayerConfig(StrategyType.OWN_FIRST, ['2H', '3C', '4S']),
            PlayerConfig(StrategyType.OWN_FIRST, ['5D', '6H']),
        ]
    )
    assert config1.cards_distribution == CardsDistribution.FIXED
    assert config1.deck is None
    assert config1.players[0].cards == ['2H', '3C', '4S']
    assert config1.players[1].cards == ['5D', '6H']

    with pytest.raises(ValueError) as err_info:
        GameConfig(
            cards_distribution=CardsDistribution.FIXED,
            players=[
                PlayerConfig(StrategyType.OWN_FIRST, ['2H', '3C', '4S']),
                PlayerConfig(StrategyType.OWN_FIRST, None),
            ]
        )

    assert str(err_info.value) == (
        "Property 'cards_distribution' is set to 'FIXED' and not all players have 'cards' property set."
    )

    with pytest.raises(ValueError) as err_info2:
        GameConfig(
            cards_distribution=CardsDistribution.FIXED,
            players=[
                PlayerConfig(StrategyType.OWN_FIRST, ['2H', '3C', '4S']),
                PlayerConfig(StrategyType.OWN_FIRST, []),
            ]
        )

    assert str(err_info2.value) == (
        "Property 'cards_distribution' is set to 'FIXED' and not all players have 'cards' property set."
    )


def test_card_distribution_random() -> None:
    config1 = GameConfig(
        cards_distribution=CardsDistribution.RANDOM,
        deck=['2H', '3C', '4S', '5D', '6H', '7C', '8S', '9D', '10H', 'JC', 'QS', 'KD', 'AH'],
        players=[
            PlayerConfig(StrategyType.OWN_FIRST, ['2H', '3C', '4S']),
            PlayerConfig(StrategyType.OWN_FIRST, ['5D', '6H']),
        ]
    )
    assert config1.cards_distribution == CardsDistribution.RANDOM
    assert config1.deck == ['2H', '3C', '4S', '5D', '6H', '7C', '8S', '9D', '10H', 'JC', 'QS', 'KD', 'AH']
    assert config1.players[0].cards is None
    assert config1.players[1].cards is None

    with pytest.raises(ValueError) as err_info:
        GameConfig(
            cards_distribution=CardsDistribution.RANDOM,
            deck=None
        )

    assert str(err_info.value) == (
        "Property 'cards_distribution' is set to 'RANDOM'. 'deck' property is None."
    )

    with pytest.raises(ValueError) as err_info2:
        GameConfig(
            cards_distribution=CardsDistribution.RANDOM,
            deck=[]
        )

    assert str(err_info2.value) == (
        "Property 'cards_distribution' is set to 'RANDOM'. 'deck' property is an empty list."
    )
