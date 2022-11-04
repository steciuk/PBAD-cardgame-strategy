from simulation.deck.card import Card
from simulation.deck.deck import Deck
from simulation.game.player.player import Player
from simulation.game_config.configs import GameConfig


class OwnLastPlayer(Player):
    def __init__(self, id: int, deck: Deck, game_config: GameConfig) -> None:
        super().__init__(id, deck, game_config)

    def strategy(self, to_collect: dict[int, list[Card]]) -> list[Card]:
        """
        Collects the cards of other players in order of their ids, then own cards. (in the order of cards played)
        """
        my_cards: list[Card] = to_collect[self.id]
        player_ids: list[int] = sorted(to_collect.keys())
        other_cards = [card for id in player_ids for card in to_collect[id] if id != self.id]
        return [*other_cards, *my_cards]
