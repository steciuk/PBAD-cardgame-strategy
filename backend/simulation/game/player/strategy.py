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
    def strategy(
        self,
        player_states: list[PlayerState],
        to_collect: dict[int, list[Card]]
    ) -> list[Card]:
        pass

    def collect(self, game_state: GameState) -> list[Card]:
        if game_state.to_collect is None:
            return []

        to_collect_in_order = self.strategy(game_state.players_states, game_state.to_collect[1])

        if collections.Counter(
            [card for cards in game_state.to_collect[1].values() for card in cards]
        ) != collections.Counter(to_collect_in_order):
            raise ValueError('Invalid strategy. Not all cards were collected.')

        return self.strategy(game_state.players_states, game_state.to_collect[1])
