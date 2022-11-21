import random

from simulation.deck.card import Card
from simulation.game.player.strategy import Strategy
from simulation.game.state.game_state import GameState
from simulation.game_config.configs import GameConfig
from simulation.game_config.enums import StrategyType


class RandomPlayersStrategy(Strategy):
    def __init__(self, id: int, game_config: GameConfig) -> None:
        super().__init__(id, game_config)

    @property
    def strategy_type(self) -> StrategyType:
        return StrategyType.RANDOM_PLAYERS

    def collect(
        self,
        game_state: GameState
    ) -> list[Card]:
        """
        Collects the cards in random order of the players. (in the order of cards played)
        """
        to_collect: dict[int, list[Card]] = game_state.to_collect_by_id[1]
        player_ids: list[int] = list(to_collect.keys())
        random.shuffle(player_ids)
        cards = [card for id in player_ids for card in to_collect[id]]
        return cards
