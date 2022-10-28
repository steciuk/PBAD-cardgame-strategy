import collections
from abc import ABC, abstractmethod

from simulation.deck.card import Card
from simulation.deck.deck import Deck
from simulation.game_config.configs import GameConfig


class Player(ABC):
    def __init__(self, id: int, deck: Deck, game_config: GameConfig) -> None:
        self._id: int = id
        self._num_cards_in_war: int = game_config.rules.num_cards_in_war
        self._deck: Deck = deck
        self.lost: bool = False

    @property
    def id(self) -> int:
        return self._id

    @abstractmethod
    def strategy(self, to_collect: dict[int, list[Card]]) -> list[Card]:
        pass

    @property
    def num_cards(self) -> int:
        return self._deck.size

    def play(self) -> Card:
        return self._deck.pop_top()

    def can_war(self) -> bool:
        return self._deck.size > self._num_cards_in_war

    def war(self) -> list[Card]:
        return self._deck.pop_n_top(min(self._num_cards_in_war, self._deck.size))

    # Probably it will have to take some kind of game state as an argument.
    def collect(self, to_collect: dict[int, list[Card]]) -> None:
        to_collect_in_order: list[Card] = self.strategy(to_collect)

        if collections.Counter(
            [card for cards in to_collect.values() for card in cards]
        ) != collections.Counter(to_collect_in_order):
            raise Exception('Invalid strategy. Cards were not collected properly.')

        self._deck.push_bottom(to_collect_in_order)

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Player) and self.id == other.id
