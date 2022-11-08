import collections
from abc import ABC, abstractmethod

from simulation.deck.card import Card
from simulation.deck.deck import Deck
from simulation.game.state.game_state import GameState
from simulation.game_config.configs import GameConfig


class Player(ABC):
    def __init__(self, id: int, game_config: GameConfig) -> None:
        self.id: int = id

    @abstractmethod
    def strategy(self, game_state: GameState) -> list[Card]:
        pass

    def _to_collect_or_none(self, game_state: GameState) -> dict[int, list[Card]] | None:
        return game_state.to_collect[1] if game_state.to_collect is not None else None
