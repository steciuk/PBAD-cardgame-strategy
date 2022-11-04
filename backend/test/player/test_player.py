import pytest

from simulation.deck.card import Card
from simulation.deck.deck import Deck
from simulation.game.player.player import Player
from simulation.game_config.configs import GameConfig, RulesConfig
from simulation.utils.deck.utils import cards_to_codes

# helpers


class MockPlayer(Player):
    def __init__(self, id: int, deck: Deck, game_config: GameConfig) -> None:
        super().__init__(id, deck, game_config)

    def strategy(self, to_collect: dict[int, list[Card]]) -> list[Card]:
        """
        Intentionally incorrect strategy.
        """
        return to_collect[0]

# tests


def test_init() -> None:
    player = MockPlayer(0, Deck(), GameConfig())
    assert player.id == 0
    assert player.lost == False


def can_war() -> None:
    player1 = MockPlayer(0, Deck(), GameConfig(rules=RulesConfig(num_cards_in_war=2)))
    assert player1.can_war() == False

    player2 = MockPlayer(0, Deck([Card('2H'), Card('2H')]), GameConfig(rules=RulesConfig(num_cards_in_war=2)))
    assert player2.can_war() == False

    player3 = MockPlayer(
        0,
        Deck([Card('2H'), Card('2H'), Card('2H')]),
        GameConfig(rules=RulesConfig(num_cards_in_war=2))
    )
    assert player3.can_war() == True


def test_war() -> None:
    player1 = MockPlayer(
        0,
        Deck([Card('2H'), Card('3D'), Card('4S')]),
        GameConfig(rules=RulesConfig(num_cards_in_war=2))
    )
    assert cards_to_codes(player1.war()) == ['2H', '3D']

    player2 = MockPlayer(
        0,
        Deck([Card('2H'), Card('3D'), Card('4S')]),
        GameConfig(rules=RulesConfig(num_cards_in_war=1))
    )
    assert cards_to_codes(player2.war()) == ['2H']


def test_collect() -> None:
    player1 = MockPlayer(1, Deck(), GameConfig())
    to_collect = {
        0: [Card('2H'), Card('3C'), Card('4S')],
        1: [Card('5D'), Card('6H')],
        2: [Card('7S'), Card('8D')]
    }

    with pytest.raises(ValueError) as err_info:
        player1.collect(to_collect)

    assert str(err_info.value) == 'Invalid strategy. Cards were not collected properly.'
