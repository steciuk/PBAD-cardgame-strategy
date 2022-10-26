from simulation.card import Card


def cards_to_codes(cards: list[Card]) -> list[str]:
    return [card.code for card in cards]
