# import pytest

import random

from simulation.deck.card import Card
from simulation.deck.deck import Deck
from simulation.game.player.strategies.random_players import RandomPlayersPlayer
from simulation.game_config.configs import GameConfig
from simulation.utils.deck.utils import cards_to_codes


def test_strategy() -> None:
    random.seed(0)
    player = RandomPlayersPlayer(0, Deck(), GameConfig())
    to_collect1 = {
        1: [Card('2H'), Card('3C'), Card('4S')],
        2: [Card('5D'), Card('6H')]
    }
    assert cards_to_codes(player.strategy(to_collect1)) == ['2H', '3C', '4S', '5D', '6H']

    to_collect2 = {
        5: [Card('JH'), Card('QC')],
        1: [Card('2H'), Card('3C'), Card('4S')],
        2: [Card('5D'), Card('6H')],
        4: [Card('9C'), Card('TS')],
        3: [Card('7S'), Card('8D')]
    }
    assert cards_to_codes(player.strategy(to_collect2)) == [
        '7S', '8D', '5D', '6H', '2H', '3C', '4S', 'JH', 'QC', '9C', 'TS'
    ]
