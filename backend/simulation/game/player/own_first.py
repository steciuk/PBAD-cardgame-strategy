from simulation.deck.card import Card
from simulation.deck.deck import Deck
from simulation.game.player.player import Player
from simulation.game_config.configs import GameConfig


class OwnFirstPlayer(Player):
    def __init__(self, id: int, deck: Deck, game_config: GameConfig) -> None:
        super().__init__(id, deck, game_config)

    def strategy(self, to_collect: dict[int, list[Card]]) -> list[Card]:
        """
        Collects own cards first, then the cards of other players in order of their ids.
        """
        my_cards: list[Card] = to_collect[self.id]
        player_ids: list[int] = sorted(to_collect.keys())
        other_cards = [card for id in player_ids for card in to_collect[id] if id != self.id]
        return [*my_cards, *other_cards]
