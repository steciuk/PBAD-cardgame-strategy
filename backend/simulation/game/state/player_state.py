from simulation.deck.deck import Deck
from simulation.game_config.enums import StrategyType


class PlayerState:
    def __init__(self, id: int, deck: Deck, strategy: StrategyType, lost: bool = False) -> None:
        self.id: int = id
        self.deck: Deck = deck
        self.strategy: StrategyType = strategy
        self.lost: bool = lost
