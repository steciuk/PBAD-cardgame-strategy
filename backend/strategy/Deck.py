import random

from strategy.card import Card
from strategy.utils.card.consts import RANKS_LIST, SUITS_LIST


class Deck:
    def __init__(self, cards: list[Card] = []) -> None:
        self._cards = cards.copy()

    @property
    def cards(self) -> list[Card]:
        return self._cards.copy()

    @property
    def size(self) -> int:
        return len(self._cards)

    @property
    def weight(self) -> int:
        return sum(card.weight for card in self._cards)

    def full(self) -> None:
        self._cards = [Card(rank, suit)
                       for rank in RANKS_LIST for suit in SUITS_LIST]

    def empty(self) -> None:
        self._cards = []

    def fill_with_n_random(self, n: int) -> None:
        if n > 52 or n < 0:
            raise ValueError(f'illegal number of cards to fill: {n}')

        self.full()
        self.shuffle()
        self.pop_n_top(52 - n)

    def shuffle(self) -> None:
        random.shuffle(self._cards)

    def pop_top(self) -> Card:
        if len(self._cards) == 0:
            raise IndexError('cannot pop, deck is empty')

        return self._cards.pop(0)

    def pop_n_top(self, n: int) -> list[Card]:
        if n > len(self._cards):
            raise IndexError(
                f'cannot pop {n} cards, deck has only {len(self._cards)}')
        elif n < 0:
            raise ValueError(f'illegal number of cards to pop: {n}')

        popped = self._cards[:n]
        self._cards = self._cards[n:]
        return popped
