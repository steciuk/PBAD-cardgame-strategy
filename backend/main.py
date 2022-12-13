import time
import random

from simulation.deck.card import Card
from simulation.deck.deck import Deck
from simulation.game.game import Game
from simulation.game.simulator import SimulatorV2
from simulation.game.state.game_state import GameState
from simulation.game.state.player_state import PlayerState
from simulation.game_config.configs import GameConfig, PlayerConfig, RulesConfig
from simulation.game_config.enums import CardsDistribution, DeckType, StrategyType
from simulation.utils.experiments import random_game_box_plot, balanced_deck_scenario


STRATEGIES_LIST = [
    StrategyType.OWN_FIRST,
    StrategyType.OWN_LAST,
    StrategyType.RANDOM_CARDS,
    StrategyType.RANDOM_PLAYERS,
    # StrategyType.GREEDY,
    StrategyType.GREEDY_GROUPED_BY_6,
    StrategyType.GREEDY_RANDOM_PERMUTATIONS_10000,
    StrategyType.GREEDY_RANDOM_PERMUTATIONS_100,
    StrategyType.GREEDY_RANDOM_PERMUTATIONS_2,
    StrategyType.GROWING,
    StrategyType.DECREASING
]

CONSTANTS_STRATEGIES = [
    StrategyType.OWN_FIRST,
    StrategyType.OWN_LAST,
    StrategyType.GROWING,
    StrategyType.DECREASING
]


def three_players_draw_set_cards() -> None:
    config = GameConfig(
        cards_distribution=CardsDistribution.FIXED,
        deck=DeckType.HEARTS,
        players=[PlayerConfig(StrategyType.OWN_FIRST, DeckType.CLUBS),
                 PlayerConfig(StrategyType.OWN_FIRST, DeckType.DIAMONDS),
                 PlayerConfig(StrategyType.OWN_FIRST, DeckType.HEARTS)]
    )

    game = Game(config)
    game.play()


def three_players_set_cards() -> None:
    config = GameConfig(
        cards_distribution=CardsDistribution.FIXED_RANDOM,
        players=[PlayerConfig(StrategyType.OWN_FIRST, ['5S', '6S', '7S']),
                 PlayerConfig(StrategyType.OWN_FIRST, ['5S', '6S', '7S']),
                 PlayerConfig(StrategyType.OWN_FIRST, ['5S', '6S', '7S'])]
    )

    game = Game(config)
    game.play()
    game.play()
    game.play()


def four_players_random_cards() -> None:
    config = GameConfig(
        cards_distribution=CardsDistribution.RANDOM,
        players=[PlayerConfig(StrategyType.RANDOM_CARDS, None),
                 PlayerConfig(StrategyType.RANDOM_CARDS, None),
                 PlayerConfig(StrategyType.RANDOM_CARDS, None)]
    )

    game = Game(config, debug=True)
    game.play()


def four_players_random_cards_big_wars() -> None:
    config: GameConfig = GameConfig(
        cards_distribution=CardsDistribution.RANDOM,
        players=[PlayerConfig(StrategyType.RANDOM_CARDS, None),
                 PlayerConfig(StrategyType.RANDOM_CARDS, None),
                 PlayerConfig(StrategyType.RANDOM_CARDS, None),
                 PlayerConfig(StrategyType.RANDOM_CARDS, None)],
        rules=RulesConfig(num_cards_in_war=2)
    )

    game = Game(config, debug=True)
    game.play()


def each_vs_each(iterations: int = 10000) -> None:
    for strategy1 in STRATEGIES_LIST:
        for strategy2 in STRATEGIES_LIST:
            print(strategy1, strategy2)
            if strategy1 in CONSTANTS_STRATEGIES and strategy2 in CONSTANTS_STRATEGIES:
                max_turns = 20000
            else:
                max_turns = 100000
            balanced_deck_scenario(1, 1, iterations, strategy=strategy1,
                                   strategy2=strategy2, draw_box_plot=False, max_turns=max_turns)


def default() -> None:
    config = GameConfig()
    game = Game(config, debug=True)
    game.play()


if __name__ == "__main__":
    four_players_random_cards_big_wars()
