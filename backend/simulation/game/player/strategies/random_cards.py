import random

from simulation.deck.card import Card
from simulation.deck.deck import Deck
from simulation.game.player.player import Player
from simulation.game.state.game_state import GameState
from simulation.game_config.configs import GameConfig


class RandomCardsPlayer(Player):
    def __init__(self, id: int, game_config: GameConfig) -> None:
        super().__init__(id, game_config)

    def strategy(self, game_state: GameState) -> list[Card]:
        """
        Collects all cards randomly.
        """
        to_collect = self._to_collect_or_none(game_state)
        if to_collect is None:
            return []

        all_cards = [card for cards in to_collect.values() for card in cards]
        random.shuffle(all_cards)
        return all_cards
