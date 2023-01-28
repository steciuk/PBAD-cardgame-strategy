from simulation.deck.card import Card
from simulation.deck.deck import Deck
from simulation.game.player.strategy import Strategy
from simulation.game.state.game_state import GameState
from simulation.game.state.player_state import PlayerState
from simulation.game_config.configs import GameConfig
from simulation.game_config.enums import StrategyType


class GrowingStrategy(Strategy):
    def __init__(self, id: int, game_config: GameConfig) -> None:
        super().__init__(id, game_config)

    @property
    def strategy_type(self) -> StrategyType:
        return StrategyType.GROWING

    def collect(
        self,
        game_state: GameState
    ) -> list[Card]:
        """
        Collects own cards first, then the cards of other players in order of their ids. (in the order of cards played)
        """
        to_collect: dict[int, list[Card]] = game_state.to_collect_by_id[1]
        tmp = [to_collect[player] for player in to_collect]
        to_collect_list: list[Card] = [item for sublist in tmp for item in sublist]
        return sorted(to_collect_list)
