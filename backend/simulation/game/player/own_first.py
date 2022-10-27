from simulation.deck.card import Card
from simulation.game.player.player import Player
from simulation.game_config.configs import RulesConfig


class OwnFirstPlayer(Player):
    def __init__(self, id: int, cards: list[Card], rules_config: RulesConfig) -> None:
        super().__init__(id, cards, rules_config)

    def strategy(self, to_collect: dict[int, list[Card]]) -> list[Card]:
        """
        Collects own cards first, then the cards of other players in order of their ids.
        """
        my_cards: list[Card] = to_collect[self.id]
        player_ids: list[int] = sorted(to_collect.keys())
        other_cards = [card for id in player_ids for card in to_collect[id] if id != self.id]
        return [*my_cards, *other_cards]
