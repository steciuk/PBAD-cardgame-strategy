from collections import defaultdict
from enum import Enum
from typing import TypeAlias, Union

from simulation.deck.card import Card
from simulation.game_config.configs import RulesConfig


class TurnResult:
    def __init__(self, winner_id: int, to_collect: dict[int, list[Card]]) -> None:
        self.winner_id: int = winner_id
        self.to_collect: dict[int, list[Card]] = to_collect


class SimulatorState(Enum):
    INIT_INPUT_CARDS = 'INIT_INPUT_CARDS'
    INPUT_CARDS = 'INPUT_CARDS'
    INPUT_WAR = 'INPUT_WAR'
    RECEIVE_RESULT = 'RECEIVE_RESULT'


class Simulator:
    def __init__(
        self,
        rules_config: RulesConfig,
        to_collect: defaultdict[int, list[Card]] = defaultdict(list),
        state: SimulatorState = SimulatorState.INIT_INPUT_CARDS,
        winner_id: Union[int, None] = None,
        # fighting_players_ids: list[int] = [] TODO: analyze if needed
    ) -> None:
        self._rules_config: RulesConfig = rules_config
        self._to_collect: defaultdict[int, list[Card]] = to_collect
        self._state: SimulatorState = state
        self._winner_id: Union[int, None] = winner_id
        # self._fighting_players_ids: list[int] = fighting_players_ids

    @property
    def state(self) -> SimulatorState:
        return self._state

    def input_cards(self, cards_per_player: dict[int, Card]) -> list[int]:
        """
        Step the simulation by inputting the cards played by each player.
        Simulation will be in 'RECEIVE_RESULT' or 'INPUT_WAR' state after this call.

        Args:
            cards_per_player (dict[int, Card]): dict of player id to card played by that player

        Raises:
            ValueError: if the simulator is not in the 'INPUT_CARDS' state

        Returns:
            list[int]: list of player ids that take part in the war (if any)
        """
        if self._state != SimulatorState.INIT_INPUT_CARDS and self._state != SimulatorState.INPUT_CARDS:
            raise ValueError(f"Simulator is not in '{SimulatorState.INPUT_CARDS.name}' state.")

        self._to_collect = defaultdict(list)
        for player_id, card in cards_per_player.items():
            self._to_collect[player_id].append(card)

        return self._compare_cards(cards_per_player)

    def input_war(self, cards_per_player: dict[int, list[Card]]) -> list[int]:
        """
        Step the simulation by inputting the cards added by each player to the war.

        Args:
            cards_per_player (dict[int, list[Card]]): dict of player id to cards added by that player

        Raises:
            ValueError: if the simulator is not in the 'INPUT_WAR' state

        Returns:
            list[int]: list of player ids that take part in the war (if any)

        """
        if self._state != SimulatorState.INPUT_WAR:
            raise ValueError(f"Simulator is not in '{SimulatorState.INPUT_WAR.name}' state.")

        fighting_cards: dict[int, Card] = {}

        for player_id, cards in cards_per_player.items():
            self._to_collect[player_id].extend(cards)
            if len(cards) == self._rules_config.num_cards_in_war:
                fighting_cards[player_id] = cards[-1]

        return self._compare_cards(fighting_cards)

    def get_last_turn_result(self) -> TurnResult:
        """
        Receive the result of the last turn. 
        If simulation in 'RECEIVE_RESULT' must be called at least once to step the simulation.
        Simulation will be in 'INPUT_CARDS' state after this call.

        Raises:
            ValueError: if the simulation is during the turn, or before the first turn

        Returns:
            FightResult: object containing the winner id and the dict of player id to cards collected by that player
        """
        if (self._state != SimulatorState.RECEIVE_RESULT and self._state != SimulatorState.INPUT_CARDS) or self._winner_id is None:
            raise ValueError(
                f"Simulator is neither in '{SimulatorState.RECEIVE_RESULT.name}' nor in '{SimulatorState.INPUT_CARDS.name}' state."
            )

        self._state = SimulatorState.INPUT_CARDS
        return TurnResult(self._winner_id, self._to_collect)

    def clone(self) -> 'Simulator':
        return Simulator(
            self._rules_config,
            self._to_collect,
            self._state,
            self._winner_id,
            # self._fighting_players_ids
        )

    def _compare_cards(self, cards_per_player: dict[int, Card]) -> list[int]:
        highest_card: Card = max(cards_per_player.items(), key=lambda x: x[1])[1]
        fighting_players_ids = [
            i for i, card in cards_per_player.items() if card.is_same_rank(highest_card)
        ]

        if len(fighting_players_ids) == 1:
            self._winner_id = fighting_players_ids[0]
            # self._fighting_players_ids = []
            self._state = SimulatorState.RECEIVE_RESULT
            return []

        # self._fighting_players_ids = fighting_players_ids
        self._state = SimulatorState.INPUT_WAR
        return fighting_players_ids
