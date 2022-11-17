from typing import Optional

from simulation.deck.card import Card
from simulation.game.state.player_state import PlayerState


class GameState:
    def __init__(
        self,
        players_states: list[PlayerState],
        turn: int = 0,
        to_collect_by_id: tuple[Optional[int], dict[int, list[Card]]] = (None, {}),
        winner_id: Optional[int] = None,
    ) -> None:
        self.players_states: list[PlayerState] = players_states
        self.turn: int = turn
        self.to_collect_by_id: tuple[Optional[int], dict[int, list[Card]]] = to_collect_by_id
        self.winner_id: Optional[int] = winner_id

    def __str__(self) -> str:
        repr = f'turn: {self.turn}\n'
        for player_state in self.players_states:
            repr += f'{player_state}\n'

        if self.to_collect_by_id[0] is None:
            repr += 'No cards to collect\n'
        else:
            repr += f'collect by: {self.to_collect_by_id[0]}\n'
            cards_to_collect = dict(self.to_collect_by_id[1])
            repr += f'to collect: {cards_to_collect}\n'

        return repr

    def __repr__(self) -> str:
        return self.__str__()
