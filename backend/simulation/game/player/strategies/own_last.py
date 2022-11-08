from simulation.deck.card import Card
from simulation.deck.deck import Deck
from simulation.game.player.player import Player
from simulation.game.state.game_state import GameState
from simulation.game_config.configs import GameConfig


class OwnLastPlayer(Player):
    def __init__(self, id: int, game_config: GameConfig) -> None:
        super().__init__(id, game_config)

    def strategy(self, game_state: GameState) -> list[Card]:
        """
        Collects the cards of other players in order of their ids, then own cards. (in the order of cards played)
        """
        to_collect = self._to_collect_or_none(game_state)
        if to_collect is None:
            return []

        my_cards: list[Card] = to_collect[self.id]
        player_ids: list[int] = sorted(to_collect.keys())
        other_cards = [card for id in player_ids for card in to_collect[id] if id != self.id]
        return [*other_cards, *my_cards]
