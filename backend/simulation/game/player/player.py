import collections
from abc import ABC, abstractmethod

from simulation.deck.card import Card
from simulation.deck.deck import Deck
from simulation.game_config.configs import RulesConfig


class Player(ABC):
    def __init__(self, id: int, cards: list[Card], rules_config: RulesConfig) -> None:
        self._id: int = id
        self._num_cards_in_war: int = rules_config.num_cards_in_war
        self._cards: Deck = Deck(cards)

    @property
    def id(self) -> int:
        return self._id

    @abstractmethod
    def strategy(self, to_collect: dict[int, list[Card]]) -> list[Card]:
        pass

    def play(self) -> Card:
        return self._cards.pop_top()

    def can_war(self) -> bool:
        return self._cards.size > self._num_cards_in_war

    def war(self) -> list[Card]:
        return self._cards.pop_n_top(self._num_cards_in_war)

    def collect(self, to_collect: dict[int, list[Card]]) -> None:
        to_collect_in_order: list[Card] = self.strategy(to_collect)

        if collections.Counter(
                [card for cards in to_collect.values() for card in cards]) != collections.Counter(
                to_collect_in_order):
            raise Exception('Invalid strategy. Cards were not collected properly.')

        self._cards.push_bottom(to_collect_in_order)
