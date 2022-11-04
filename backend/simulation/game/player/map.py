from typing import Type

from simulation.game.player.player import Player
from simulation.game.player.strategies.own_first import OwnFirstPlayer
from simulation.game.player.strategies.own_last import OwnLastPlayer
from simulation.game.player.strategies.random_cards import RandomCardsPlayer
from simulation.game.player.strategies.random_players import RandomPlayersPlayer
from simulation.game_config.enums import Strategy

PlayersMap: dict[Strategy, Type[Player]] = {
    Strategy.OWN_FIRST: OwnFirstPlayer,
    Strategy.OWN_LAST: OwnLastPlayer,
    Strategy.RANDOM_CARDS: RandomCardsPlayer,
    Strategy.RANDOM_PLAYERS: RandomPlayersPlayer,
}
