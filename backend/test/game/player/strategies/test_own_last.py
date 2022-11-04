import pytest

from simulation.deck.card import Card
from simulation.deck.deck import Deck
from simulation.game.player.strategies.own_last import OwnLastPlayer
from simulation.game_config.configs import GameConfig
from simulation.utils.deck.utils import cards_to_codes


def test_strategy() -> None:
    player = OwnLastPlayer(1, Deck(), GameConfig())
    to_collect1 = {
        1: [Card('2H'), Card('3C'), Card('4S')],
        2: [Card('5D'), Card('6H')]
    }
    assert cards_to_codes(player.strategy(to_collect1)) == ['5D', '6H', '2H', '3C', '4S']

    to_collect2 = {
        1: [Card('2H'), Card('3C'), Card('4S')],
        2: [Card('5D'), Card('6H')],
        3: [Card('7S'), Card('8D')]
    }
    assert cards_to_codes(player.strategy(to_collect2)) == ['5D', '6H', '7S', '8D', '2H', '3C', '4S']

    to_collect3 = {
        1: [Card('2H'), Card('3C'), Card('4S')],
        2: [Card('5D'), Card('6H')],
        3: [Card('7S'), Card('8D')],
        4: [Card('9C'), Card('TS')]
    }
    assert cards_to_codes(player.strategy(to_collect3)) == [
        '5D', '6H', '7S', '8D', '9C', 'TS', '2H', '3C', '4S'
    ]

    to_collect4 = {
        5: [Card('JH'), Card('QC')],
        1: [Card('2H'), Card('3C'), Card('4S')],
        2: [Card('5D'), Card('6H')],
        4: [Card('9C'), Card('TS')],
        3: [Card('7S'), Card('8D')]
    }
    assert cards_to_codes(player.strategy(to_collect4)) == [
        '5D', '6H', '7S', '8D', '9C', 'TS', 'JH', 'QC',  '2H', '3C', '4S'
    ]
