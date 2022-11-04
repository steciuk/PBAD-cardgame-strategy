import random

from simulation.deck.card import Card
from simulation.deck.deck import Deck
from simulation.game.player.player import Player
from simulation.game_config.configs import GameConfig


class RandomCardsPlayer(Player):
    def __init__(self, id: int, deck: Deck, game_config: GameConfig) -> None:
        super().__init__(id, deck, game_config)

    def strategy(self, to_collect: dict[int, list[Card]]) -> list[Card]:
        """
        Collects all cards randomly.
        """
        all_cards = [card for cards in to_collect.values() for card in cards]
        random.shuffle(all_cards)
        return all_cards
