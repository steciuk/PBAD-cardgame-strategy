import random

from simulation.game.game import Game
from simulation.game_config.configs import GameConfig, PlayerConfig, RulesConfig
from simulation.game_config.enums import CardsDistribution, DeckType, Strategy


def three_players_draw_set_cards() -> None:
    config = GameConfig(
        cards_distribution=CardsDistribution.FIXED,
        players=[PlayerConfig(Strategy.OWN_FIRST, DeckType.CLUBS),
                 PlayerConfig(Strategy.OWN_FIRST, DeckType.DIAMONDS),
                 PlayerConfig(Strategy.OWN_FIRST, DeckType.HEARTS)]
    )

    game = Game(config)
    game.play()


def three_players_set_cards() -> None:
    config = GameConfig(
        cards_distribution=CardsDistribution.FIXED_RANDOM,
        players=[PlayerConfig(Strategy.OWN_FIRST, ['5S', '6S', '7S']),
                 PlayerConfig(Strategy.OWN_FIRST, ['5S', '6S', '7S']),
                 PlayerConfig(Strategy.OWN_FIRST, ['5S', '6S', '7S'])]
    )

    game = Game(config)
    game.play()
    game.play()
    game.play()


def four_players_random_cards_big_wars() -> None:
    config: GameConfig = GameConfig(
        cards_distribution=CardsDistribution.RANDOM,
        players=[PlayerConfig(Strategy.OWN_FIRST, None),
                 PlayerConfig(Strategy.OWN_FIRST, None),
                 PlayerConfig(Strategy.OWN_FIRST, None),
                 PlayerConfig(Strategy.OWN_FIRST, None)],
        rules=RulesConfig(num_cards_in_war=2)
    )

    game = Game(config)
    game.play()


def default() -> None:
    config = GameConfig()
    game = Game(config)
    game.play()


if __name__ == "__main__":
    three_players_set_cards()
