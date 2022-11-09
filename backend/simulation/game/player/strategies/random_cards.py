import random

from simulation.deck.card import Card
from simulation.game.player.strategy import Strategy
from simulation.game.state.game_state import GameState
from simulation.game.state.player_state import PlayerState
from simulation.game_config.configs import GameConfig
from simulation.game_config.enums import StrategyType


class RandomCardsStrategy(Strategy):
    def __init__(self, id: int, game_config: GameConfig) -> None:
        super().__init__(id, game_config)

    @property
    def strategy_type(self) -> StrategyType:
        return StrategyType.RANDOM_CARDS

    def strategy(
        self,
        player_states: list[PlayerState],
        to_collect: dict[int, list[Card]]
    ) -> list[Card]:
        """
        Collects all cards randomly.
        """
        all_cards = [card for cards in to_collect.values() for card in cards]
        random.shuffle(all_cards)
        return all_cards
