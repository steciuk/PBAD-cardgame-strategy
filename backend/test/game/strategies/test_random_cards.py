import random

import pytest

from simulation.deck.card import Card
from simulation.deck.deck import Deck
from simulation.game.player.strategies.random_cards import RandomCardsStrategy
from simulation.game.state.game_state import GameState
from simulation.game_config.configs import GameConfig


def test_strategy() -> None:
    random.seed(0)
    PLAYER_ID = 0
    strategy = RandomCardsStrategy(PLAYER_ID, GameConfig())
    game_state = GameState(players_states=[], to_collect=(PLAYER_ID, {
        4: [Card('JH'), Card('QC')],
        0: [Card('2H'), Card('3C'), Card('4S')],
        1: [Card('5D'), Card('6H')],
        3: [Card('9C'), Card('TS')],
        2: [Card('7S'), Card('8D')]
    }))

    assert strategy.collect(game_state) == [
        Card('5D'),
        Card('4S'),
        Card('8D'),
        Card('6H'),
        Card('JH'),
        Card('QC'),
        Card('9C'),
        Card('2H'),
        Card('TS'),
        Card('3C'),
        Card('7S')
    ]
