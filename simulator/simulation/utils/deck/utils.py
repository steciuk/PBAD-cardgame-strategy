from simulation.deck.card import Card
from simulation.game_config.enums import DeckType
from simulation.utils.deck.consts import BLACK, RANKS_LIST, RED, SUITS_LIST


def cards_to_codes(cards: list[Card]) -> list[str]:
    return [card.code for card in cards]


def codes_to_cards(codes: list[str]) -> list[Card]:
    return [Card(code) for code in codes]


def get_cards_list_of_type(deck_type: DeckType) -> list[Card]:
    if deck_type == DeckType.FULL:
        return [Card(rank, suit) for rank in RANKS_LIST for suit in SUITS_LIST]
    elif deck_type == DeckType.RED:
        return [Card(rank, suit) for rank in RANKS_LIST for suit in RED]
    elif deck_type == DeckType.BLACK:
        return [Card(rank, suit) for rank in RANKS_LIST for suit in BLACK]
    elif deck_type == DeckType.HEARTS:
        return [Card(rank, 'H') for rank in RANKS_LIST]
    elif deck_type == DeckType.DIAMONDS:
        return [Card(rank, 'D') for rank in RANKS_LIST]
    elif deck_type == DeckType.SPADES:
        return [Card(rank, 'S') for rank in RANKS_LIST]
    elif deck_type == DeckType.CLUBS:
        return [Card(rank, 'C') for rank in RANKS_LIST]
    else:
        raise ValueError(f'unknown deck type: {deck_type}')
