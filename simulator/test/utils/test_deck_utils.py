import pytest

from simulation.deck.card import Card
from simulation.game_config.enums import DeckType
from simulation.utils.deck.utils import (
    cards_to_codes,
    codes_to_cards,
    get_cards_list_of_type,
)


def test_cards_to_codes() -> None:
    cards1 = [Card('2H'), Card('3C'), Card('4S'), Card('5D'), Card('6H')]
    assert cards_to_codes(cards1) == ['2H', '3C', '4S', '5D', '6H']

    cards2: list[Card] = []
    assert cards_to_codes(cards2) == []


def test_codes_to_cards() -> None:
    codes1 = ['2H', '3C', '4S', '5D', '6H']
    assert codes_to_cards(codes1) == [Card('2H'), Card('3C'), Card('4S'), Card('5D'), Card('6H')]

    codes2: list[str] = []
    assert codes_to_cards(codes2) == []


def test_get_cards_list_of_type() -> None:
    assert cards_to_codes(get_cards_list_of_type(DeckType.FULL)) == [
        '2H', '2D', '2S', '2C', '3H', '3D', '3S', '3C', '4H', '4D', '4S', '4C', '5H', '5D', '5S', '5C', '6H',
        '6D', '6S', '6C', '7H', '7D', '7S', '7C', '8H', '8D', '8S', '8C', '9H', '9D', '9S', '9C', 'TH', 'TD',
        'TS', 'TC', 'JH', 'JD', 'JS', 'JC', 'QH', 'QD', 'QS', 'QC', 'KH', 'KD', 'KS', 'KC', 'AH', 'AD', 'AS',
        'AC'
    ]

    assert cards_to_codes(get_cards_list_of_type(DeckType.RED)) == [
        '2H', '2D', '3H', '3D', '4H', '4D', '5H', '5D', '6H', '6D', '7H', '7D', '8H', '8D', '9H', '9D', 'TH',
        'TD', 'JH', 'JD', 'QH', 'QD', 'KH', 'KD', 'AH', 'AD'
    ]

    assert cards_to_codes(get_cards_list_of_type(DeckType.BLACK)) == [
        '2S', '2C', '3S', '3C', '4S', '4C', '5S', '5C', '6S', '6C', '7S', '7C', '8S', '8C', '9S', '9C', 'TS',
        'TC', 'JS', 'JC', 'QS', 'QC', 'KS', 'KC', 'AS', 'AC'
    ]

    assert cards_to_codes(get_cards_list_of_type(DeckType.HEARTS)) == [
        '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', 'TH', 'JH', 'QH', 'KH', 'AH'
    ]

    assert cards_to_codes(get_cards_list_of_type(DeckType.DIAMONDS)) == [
        '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', 'TD', 'JD', 'QD', 'KD', 'AD'
    ]

    assert cards_to_codes(get_cards_list_of_type(DeckType.SPADES)) == [
        '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', 'TS', 'JS', 'QS', 'KS', 'AS'
    ]

    assert cards_to_codes(get_cards_list_of_type(DeckType.CLUBS)) == [
        '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', 'TC', 'JC', 'QC', 'KC', 'AC'
    ]

    with pytest.raises(ValueError) as err_info:
        get_cards_list_of_type('invalid')  # type: ignore

    assert str(err_info.value) == 'unknown deck type: invalid'
