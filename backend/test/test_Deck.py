from random import shuffle
from typing import Any
import pytest
from strategy.Card import Card

from strategy.Deck import Deck
import numpy as np

ALL_CARD_CODES_IN_ORDER: list[str] = ['2H', '2D', '2S', '2C', '3H', '3D', '3S', '3C', '4H', '4D', '4S', '4C', '5H',
                                      '5D', '5S', '5C', '6H', '6D', '6S', '6C', '7H', '7D', '7S', '7C', '8H', '8D',
                                      '8S', '8C', '9H', '9D', '9S', '9C', 'TH', 'TD', 'TS', 'TC', 'JH', 'JD', 'JS',
                                      'JC', 'QH', 'QD', 'QS', 'QC', 'KH', 'KD', 'KS', 'KC', 'AH', 'AD', 'AS', 'AC']

# Helpers


def verify_cards_array_content(answer: list[Card], expected: list[str]) -> Any:
    # no idea why typing the return as bool makes mypy angry :c
    answer_codes: list[str] = [card.code for card in answer]
    return np.array_equal(answer_codes, expected)

# TCs


def test_cards() -> None:
    deck1 = Deck()
    assert np.array_equal(deck1.cards, [])

    deck2 = Deck([Card('2H'), Card('3C'), Card('4S')])
    assert verify_cards_array_content(deck2.cards, ['2H', '3C', '4S']) == True


def test_size() -> None:
    deck1 = Deck()
    assert deck1.size == 0

    deck2 = Deck([Card('2H'), Card('3C'), Card('4S')])
    assert deck2.size == 3


def test_weight() -> None:
    deck1 = Deck()
    assert deck1.weight == 0

    deck2 = Deck([Card('2H'), Card('3C'), Card('4S')])
    assert deck2.weight == -15


def test_full() -> None:
    deck1 = Deck()
    deck1.full()
    assert verify_cards_array_content(
        deck1.cards, ALL_CARD_CODES_IN_ORDER) == True


def test_empty() -> None:
    deck1 = Deck()
    deck1.full()
    deck1.empty()
    assert deck1.size == 0


def test_shuffle() -> None:
    deck1 = Deck()
    deck1.full()
    deck1.shuffle()
    assert deck1.size == 52
    assert verify_cards_array_content(
        deck1.cards, ALL_CARD_CODES_IN_ORDER) == False


def pop_top() -> None:
    deck1 = Deck([Card('2H'), Card('3C'), Card('4S')])
    card1 = deck1.pop_top()
    card2 = deck1.pop_top()
    card3 = deck1.pop_top()
    assert card1.code == '2H'
    assert card2.code == '3C'
    assert card3.code == '4S'

    with pytest.raises(IndexError):
        deck1.pop_top()


def test_pop_n_top() -> None:
    deck1 = Deck([Card('2H'), Card('3C'), Card('4S'), Card('KD')])
    cards1 = deck1.pop_n_top(2)
    assert verify_cards_array_content(cards1, ['2H', '3C']) == True
    assert verify_cards_array_content(deck1.cards, ['4S', 'KD']) == True

    deck2 = Deck([Card('2H'), Card('3C'), Card('4S')])
    with pytest.raises(IndexError):
        deck2.pop_n_top(6)

    with pytest.raises(ValueError):
        deck2.pop_n_top(-6)


def fill_with_n_random() -> None:
    deck1 = Deck()
    deck1.fill_with_n_random(3)
    assert deck1.size == 3

    with pytest.raises(ValueError):
        deck1.fill_with_n_random(-6)

    with pytest.raises(ValueError):
        deck1.fill_with_n_random(100)
