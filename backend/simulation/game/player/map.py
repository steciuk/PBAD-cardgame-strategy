from typing import Type

from simulation.game.player.strategies.own_first import OwnFirstStrategy
from simulation.game.player.strategies.own_last import OwnLastStrategy
from simulation.game.player.strategies.random_cards import RandomCardsStrategy
from simulation.game.player.strategies.random_players import RandomPlayersStrategy
from simulation.game.player.strategies.greedy import GreedyStrategy
from simulation.game.player.strategies.greedy_grouped_by_6 import GreedyStrategyGroupedBy6
from simulation.game.player.strategies.greedy_random_permutations import GreedyRandomPermutations
from simulation.game.player.strategies.growing import GrowingStrategy
from simulation.game.player.strategies.decreasing import DecreasingStrategy
from simulation.game.player.strategy import Strategy
from simulation.game.state.game_state import GameState
from simulation.game_config.configs import GameConfig
from simulation.game_config.enums import StrategyType

StrategiesMap: dict[StrategyType, Type[Strategy]] = {
    StrategyType.OWN_FIRST: OwnFirstStrategy,
    StrategyType.OWN_LAST: OwnLastStrategy,
    StrategyType.RANDOM_CARDS: RandomCardsStrategy,
    StrategyType.RANDOM_PLAYERS: RandomPlayersStrategy,
    StrategyType.GREEDY: GreedyStrategy,
    StrategyType.GREEDY_GROUPED_BY_6: GreedyStrategyGroupedBy6,
    StrategyType.GREEDY_RANDOM_PERMUTATIONS: GreedyRandomPermutations,
    StrategyType.GROWING: GrowingStrategy,
    StrategyType.DECREASING: DecreasingStrategy, 
}


def get_strategy(strategy_type: StrategyType) -> Type[Strategy]:
    strategy: Type[Strategy] | None = StrategiesMap.get(strategy_type)
    if strategy is None:
        raise ValueError(f"Strategy {strategy_type} not found")

    return strategy


def get_strategies_form_game_state(game_state: GameState, game_config: GameConfig) -> dict[int, Strategy]:
    strategies: dict[int, Strategy] = {}
    for player_state in game_state.players_states:
        strategy: Type[Strategy] = get_strategy(player_state.strategy)
        strategies[player_state.id] = strategy(player_state.id, game_config)

    return strategies
