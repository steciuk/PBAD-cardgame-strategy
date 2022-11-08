from collections import defaultdict

from simulation.game.player.map import get_strategies_form_game_state
from simulation.game.player.strategy import Strategy
from simulation.game.simulator import SimulatorV2
from simulation.game.state.game_state import GameState
from simulation.game.state.player_state import PlayerState
from simulation.game_config.configs import GameConfig
from simulation.utils.state.init_player_state import init_player_states


class Game():
    def __init__(self, config: GameConfig, debug: bool = False) -> None:
        self._config: GameConfig = config
        self._debug: bool = debug

    def play(self) -> None:
        starting_player_states: list[PlayerState] = init_player_states(self._config)
        game_state: GameState = GameState(starting_player_states)
        player_strategies: dict[int, Strategy] = get_strategies_form_game_state(
            game_state, self._config
        )

        simulator = SimulatorV2(self._config, game_state)

        while game_state.winner_id is None:
            if self._debug:
                print(game_state)

            collected_cards = [] if game_state.to_collect is None else player_strategies[
                game_state.to_collect[0]
            ].collect(game_state)

            game_state = simulator.turn(collected_cards)

        if self._debug:
            print(game_state)

        print(f"Player {game_state.winner_id} won!")
