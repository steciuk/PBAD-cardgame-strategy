from simulation.deck.deck import Deck
from simulation.game_config.enums import StrategyType


class PlayerState:
    def __init__(self, id: int, deck: Deck, strategy: StrategyType) -> None:
        self.id: int = id
        self.deck: Deck = deck
        self.strategy: StrategyType = strategy

    def __str__(self) -> str:
        return f"{self.id} - {self.strategy.name} - {self.deck}"

    def __repr__(self) -> str:
        return self.__str__()
