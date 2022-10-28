import os

from definitions import ROOT_DIR
from simulation import game
from simulation.deck.card import Card
from simulation.deck.deck import Deck
from simulation.game.game import Game
from simulation.game_config.builder import GameConfigBuilder
from simulation.game_config.configs import GameConfig, PlayerConfig, RulesConfig
from simulation.game_config.enums import CardsDistribution, DeckType, Strategy


def three_players_draw_set_cards() -> None:
    config = GameConfigBuilder().with_cards_distribution(CardsDistribution.FIXED).with_players(
        [PlayerConfig(Strategy.OWN_FIRST, DeckType.CLUBS),
         PlayerConfig(Strategy.OWN_FIRST, DeckType.DIAMONDS),
         PlayerConfig(Strategy.OWN_FIRST, DeckType.HEARTS)]).build()

    game = Game(config)
    game.play()


def three_players_set_cards() -> None:
    config = GameConfigBuilder().with_cards_distribution(CardsDistribution.FIXED_RANDOM).with_players(
        [PlayerConfig(Strategy.OWN_FIRST, ['5S', '6S', '7S']),
         PlayerConfig(Strategy.OWN_FIRST, ['5S', '6S', '7S']),
         PlayerConfig(Strategy.OWN_FIRST, ['5S', '6S', '7S'])]).build()

    game = Game(config)
    game.play()


def four_players_random_cards_big_wars() -> None:
    config = GameConfigBuilder().with_cards_distribution(CardsDistribution.RANDOM).with_players(
        [PlayerConfig(Strategy.OWN_FIRST, None),
         PlayerConfig(Strategy.OWN_FIRST, None),
         PlayerConfig(Strategy.OWN_FIRST, None),
         PlayerConfig(Strategy.OWN_FIRST, None)]).with_rules(RulesConfig(num_cards_in_war=2)).build()

    game = Game(config)
    game.play()


def default() -> None:
    config = GameConfigBuilder().build()
    game = Game(config)
    game.play()


if __name__ == "__main__":
    four_players_random_cards_big_wars()
