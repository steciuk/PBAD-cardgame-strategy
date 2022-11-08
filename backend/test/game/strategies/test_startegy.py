import pytest

from simulation.deck.card import Card
from simulation.deck.deck import Deck
from simulation.game.player.strategy import Strategy
from simulation.game.state.game_state import GameState
from simulation.game.state.player_state import PlayerState
from simulation.game_config.configs import GameConfig
from simulation.game_config.enums import StrategyType


class MockStrategy(Strategy):
    def __init__(self, id: int) -> None:
        super().__init__(id, GameConfig())

    @property
    def strategy_type(self) -> StrategyType:
        return StrategyType.OWN_LAST

    def strategy(
        self,
        player_states: list[PlayerState],
        to_collect: dict[int, list[Card]]
    ) -> list[Card]:
        return []


def test_strategy() -> None:
    strategy: MockStrategy = MockStrategy(0)
    game_state_1 = GameState(players_states=[], to_collect=None)

    assert strategy.strategy_type == StrategyType.OWN_LAST
    assert strategy.collect(game_state_1) == []

    game_state_2 = GameState(players_states=[], to_collect=(0, {0: [Card('2H')]}))

    with pytest.raises(ValueError) as err_info:
        strategy.collect(game_state_2)

    assert str(err_info.value) == 'Invalid strategy. Not all cards were collected.'
