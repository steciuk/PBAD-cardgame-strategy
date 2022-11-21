import random

from simulation.deck.card import Card
from simulation.game.player.strategy import Strategy
from simulation.game.state.game_state import GameState
from simulation.game_config.configs import GameConfig
from simulation.game_config.enums import StrategyType


class RandomCardsStrategy(Strategy):
    def __init__(self, id: int, game_config: GameConfig) -> None:
        super().__init__(id, game_config)

    @property
    def strategy_type(self) -> StrategyType:
        return StrategyType.RANDOM_CARDS

    def collect(
        self,
        game_state: GameState
    ) -> list[Card]:
        """
        Collects all cards randomly.
        """
        to_collect: dict[int, list[Card]] = game_state.to_collect_by_id[1]
        all_cards: list[Card] = [card for cards in to_collect.values() for card in cards]
        random.shuffle(all_cards)
        return all_cards
