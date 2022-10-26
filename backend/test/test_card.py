import pytest

from simulation.card import Card


def test_init() -> None:
    card1 = Card('2', 'H')
    assert card1.suit == 'H'
    assert card1.rank == '2'
    assert card1.weight == -6

    card2 = Card('2H')
    assert card2.suit == 'H'
    assert card2.rank == '2'
    assert card2.weight == -6

    with pytest.raises(ValueError):
        Card('5', 'X')
    with pytest.raises(ValueError):
        Card('11', 'H')
    with pytest.raises(ValueError):
        Card('5X')
    with pytest.raises(ValueError):
        Card('H2')
    with pytest.raises(ValueError):
        Card('11H')
    with pytest.raises(ValueError):
        Card('2', 'H', 'X')


def test_repr() -> None:
    card1 = Card('2H')
    assert repr(card1) == '2H'


def test_eq() -> None:
    card1 = Card('2H')
    card2 = Card('2H')
    card3 = Card('2S')
    assert (card1 == card2) == True
    assert (card1 == card3) == False


def test_ne() -> None:
    card1 = Card('2H')
    card2 = Card('2H')
    card3 = Card('3S')
    assert (card1 != card2) == False
    assert (card1 != card3) == True


def test_lt() -> None:
    card1 = Card('2H')
    card2 = Card('2D')
    card3 = Card('3S')
    assert (card1 < card2) == False
    assert (card1 < card3) == True


def test_is_same_rank() -> None:
    card1 = Card('2H')
    card2 = Card('2D')
    card3 = Card('3S')

    assert card1.is_same_rank(card2) == True
    assert card1.is_same_rank(card3) == False
