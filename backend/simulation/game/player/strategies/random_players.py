import random

from simulation.deck.card import Card
from simulation.deck.deck import Deck
from simulation.game.player.player import Player
from simulation.game_config.configs import GameConfig


class RandomPlayersPlayer(Player):
    def __init__(self, id: int, deck: Deck, game_config: GameConfig) -> None:
        super().__init__(id, deck, game_config)

    def strategy(self, to_collect: dict[int, list[Card]]) -> list[Card]:
        """
        Collects the cards in random order of the players. (in the order of cards played)
        """
        player_ids: list[int] = list(to_collect.keys())
        random.shuffle(player_ids)
        cards = [card for id in player_ids for card in to_collect[id]]
        return cards
