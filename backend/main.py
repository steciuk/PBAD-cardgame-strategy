import random

from simulation.deck.card import Card
from simulation.deck.deck import Deck
from simulation.game.game import Game
from simulation.game.simulator import SimulatorV2
from simulation.game.state.game_state import GameState
from simulation.game.state.player_state import PlayerState
from simulation.game_config.configs import GameConfig, PlayerConfig, RulesConfig
from simulation.game_config.enums import CardsDistribution, DeckType, StrategyType


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


def default() -> None:
    config = GameConfig()
    game = Game(config, debug=True)
    game.play()


if __name__ == "__main__":
    four_players_random_cards_big_wars()
