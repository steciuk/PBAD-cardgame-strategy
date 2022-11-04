# import pytest

import random

from simulation.deck.card import Card
from simulation.deck.deck import Deck
from simulation.game.player.strategies.random_cards import RandomCardsPlayer
from simulation.game_config.configs import GameConfig
from simulation.utils.deck.utils import cards_to_codes


def test_strategy() -> None:
    random.seed(0)
    player = RandomCardsPlayer(0, Deck(), GameConfig())
    to_collect1 = {
        1: [Card('2H'), Card('3C'), Card('4S')],
        2: [Card('5D'), Card('6H')]
    }
    assert cards_to_codes(player.strategy(to_collect1)) == ['4S', '3C', '2H', '6H', '5D']

    to_collect2 = {
        5: [Card('JH'), Card('QC')],
        1: [Card('2H'), Card('3C'), Card('4S')],
        2: [Card('5D'), Card('6H')],
        4: [Card('9C'), Card('TS')],
        3: [Card('7S'), Card('8D')]
    }

    assert cards_to_codes(player.strategy(to_collect2)) == [
        '8D', 'JH', '5D', 'QC', '7S', '2H', '3C', '4S', '6H', '9C', 'TS'
    ]
