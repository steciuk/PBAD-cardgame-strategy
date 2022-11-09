import collections
from abc import ABC, abstractmethod

from simulation.deck.card import Card
from simulation.game.state.game_state import GameState
from simulation.game.state.player_state import PlayerState
from simulation.game_config.configs import GameConfig
from simulation.game_config.enums import StrategyType


class Strategy(ABC):
    def __init__(self, id: int, game_config: GameConfig) -> None:
        self.id: int = id

    @property
    @abstractmethod
    def strategy_type(self) -> StrategyType:
        pass

    @abstractmethod
    def collect(
        self,
        game_state: GameState
    ) -> list[Card]:
        pass
