import random

from simulation.deck.card import Card
from simulation.deck.deck import Deck
from simulation.game.player.player import Player
from simulation.game.state.game_state import GameState
from simulation.game_config.configs import GameConfig


class RandomPlayersPlayer(Player):
    def __init__(self, id: int, game_config: GameConfig) -> None:
        super().__init__(id, game_config)

    def strategy(self, game_state: GameState) -> list[Card]:
        """
        Collects the cards in random order of the players. (in the order of cards played)
        """
        to_collect = self._to_collect_or_none(game_state)
        if to_collect is None:
            return []

        player_ids: list[int] = list(to_collect.keys())
        random.shuffle(player_ids)
        cards = [card for id in player_ids for card in to_collect[id]]
        return cards
