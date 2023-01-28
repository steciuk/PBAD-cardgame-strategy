from simulation.deck.card import Card
from simulation.game.player.strategy import Strategy
from simulation.game.state.game_state import GameState
from simulation.game_config.configs import GameConfig
from simulation.game_config.enums import StrategyType


class OwnFirstStrategy(Strategy):
    def __init__(self, id: int, game_config: GameConfig) -> None:
        super().__init__(id, game_config)

    @property
    def strategy_type(self) -> StrategyType:
        return StrategyType.OWN_FIRST

    def collect(
        self,
        game_state: GameState
    ) -> list[Card]:
        """
        Collects own cards first, then the cards of other players in order of their ids. (in the order of cards played)
        """
        to_collect: dict[int, list[Card]] = game_state.to_collect_by_id[1]
        my_cards: list[Card] = to_collect[self.id]
        player_ids: list[int] = sorted(to_collect.keys())
        other_cards = [card for id in player_ids for card in to_collect[id] if id != self.id]
        return [*my_cards, *other_cards]
