from enum import Enum

from simulation.deck.card import Card
from simulation.game_config.configs import RulesConfig


class SimulatorState(Enum):
    INPUT_CARDS = 'INPUT_CARDS'
    INPUT_WAR = 'INPUT_WAR'
    COLLECT_CARDS = 'COLLECT_CARDS'
    FINISHED = 'FINISHED'


class Simulator:
    def __init__(
        self,
        rules_config: RulesConfig,
        to_collect: dict[int, list[Card]] = {},
        state: SimulatorState = SimulatorState.INPUT_CARDS,
    ) -> None:
        self._state: SimulatorState = state
        self._rules_config: RulesConfig = rules_config
        self._to_collect: dict[int, list[Card]] = to_collect

    @property
    def state(self) -> SimulatorState:
        return self._state

    def input_cards(self, cards_per_player: dict[int, Card]) -> None:
        if self._state != SimulatorState.INPUT_CARDS:
            raise ValueError(f"Simulator is not in '{SimulatorState.INPUT_CARDS.name}' state.")

        # -> War
        # -> Collect

    def input_war(self, cards_per_player: dict[int, list[Card]]) -> None:
        if self._state != SimulatorState.INPUT_WAR:
            raise ValueError(f"Simulator is not in '{SimulatorState.INPUT_WAR.name}' state.")

        # -> War
        # -> Collect
