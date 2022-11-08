from enum import Enum
from typing import Optional, Union

from simulation.deck.card import Card
from simulation.game.state.player_state import PlayerState


class GameState:
    def __init__(
        self,
        players_states: dict[int, PlayerState],
        turn: int = 0,
        to_collect: Optional[tuple[int, dict[int, list[Card]]]] = None,
        winner_id: Optional[int] = None,
    ) -> None:
        self.players_states: dict[int, PlayerState] = players_states
        self.turn: int = turn
        self.to_collect: Optional[tuple[int, dict[int, list[Card]]]] = to_collect
        self.winner_id: Optional[int] = winner_id
