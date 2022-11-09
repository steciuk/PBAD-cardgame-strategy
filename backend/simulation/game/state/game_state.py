from enum import Enum
from typing import Optional

from simulation.deck.card import Card
from simulation.game.state.player_state import PlayerState


class GameState:
    def __init__(
        self,
        players_states: list[PlayerState],
        turn: int = 0,
        to_collect_by_id: tuple[int | None, dict[int, list[Card]]] = (None, {}),
        winner_id: Optional[int] = None,
    ) -> None:
        self.players_states: list[PlayerState] = players_states
        self.turn: int = turn
        self.to_collect_by_id: tuple[int | None, dict[int, list[Card]]] = to_collect_by_id
        self.winner_id: Optional[int] = winner_id

    def __str__(self) -> str:
        repr = f'turn: {self.turn}\n'
        for player_state in self.players_states:
            repr += f'{player_state}\n'

        if self.to_collect_by_id is not None:
            repr += f'to_collect: {self.to_collect_by_id}\n'

        return repr

    def __repr__(self) -> str:
        return self.__str__()
