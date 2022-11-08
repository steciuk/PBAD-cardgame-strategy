from typing import Type

from simulation.game.player.player import Player
from simulation.game.player.strategies.own_first import OwnFirstPlayer
from simulation.game.player.strategies.own_last import OwnLastPlayer
from simulation.game.player.strategies.random_cards import RandomCardsPlayer
from simulation.game.player.strategies.random_players import RandomPlayersPlayer
from simulation.game_config.enums import StrategyType

PlayersMap: dict[StrategyType, Type[Player]] = {
    StrategyType.OWN_FIRST: OwnFirstPlayer,
    StrategyType.OWN_LAST: OwnLastPlayer,
    StrategyType.RANDOM_CARDS: RandomCardsPlayer,
    StrategyType.RANDOM_PLAYERS: RandomPlayersPlayer,
}
