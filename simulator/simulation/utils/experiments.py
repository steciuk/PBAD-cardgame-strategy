import math
import time
from typing import Optional
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

from simulation.game.game import Game
from simulation.game_config.configs import GameConfig, PlayerConfig, RulesConfig
from simulation.game_config.enums import CardsDistribution, DeckType, StrategyType
from matplotlib.ticker import PercentFormatter
from decimal import Decimal



def random_game_box_plot(samples: int, ranges: int, plays_in_range: int) -> None:
    data: dict[int, list[float]] = {}
    config = GameConfig(players=[PlayerConfig(StrategyType.RANDOM_CARDS, None),
                        PlayerConfig(StrategyType.RANDOM_CARDS, None)], max_turns=100000)
    for i in range(samples):
        print('\n', i)
        looses: int = 0
        wins: int = 0
        for _ in range(ranges):
            for _ in range(plays_in_range):
                game = Game(config, debug=False)
                game.play()
                if game.game_state.winner_id == 0:
                    wins += 1
                elif game.game_state.winner_id == 1:
                    looses += 1
            print(wins + looses, "wins: ", wins / (wins + looses))
            if wins + looses in data:
                data[wins+looses].append(wins / (wins + looses))
            else:
                data[wins+looses] = [wins / (wins + looses)]
    fig, ax = plt.subplots()
    ax.boxplot(np.array(list(data.values())), labels=[x * plays_in_range for x in range(1, ranges + 1)])
    plt.show()


def balanced_deck_scenario(
        samples: int, ranges: int, plays_in_range: int, strategy: StrategyType,
        strategy2: StrategyType = StrategyType.RANDOM_CARDS, draw_box_plot: bool = True,
        draw_turns_hist: bool = False, draw_wars_hist: bool = False, max_turns: Optional[int] = None) -> None:
    data: dict[int, list[float]] = {}
    config = GameConfig(
        players=[
            PlayerConfig(
                strategy,
                DeckType.BLACK,),
            PlayerConfig(
                strategy2,
                DeckType.RED)],
        cards_distribution=CardsDistribution.FIXED_RANDOM, max_turns=max_turns)
    turns_list: list[int] = []
    looses: int = 0
    wins: int = 0
    start = time.time()
    wars = []

    for i in range(samples):
        looses = 0
        wins = 0
        for j in range(ranges):
            # print(i, j)
            for i in range(plays_in_range):
                game = Game(config, debug=False)
                game.play()
                if game.game_state.winner_id == 0:
                    wins += 1
                elif game.game_state.winner_id == 1:
                    looses += 1
                turns_list.append(game.game_state.turn)
                if draw_wars_hist:
                    wars_dict = game.game_state.wars_number
                    for cards_number in wars_dict:
                        for _ in range(wars_dict[cards_number]):
                            if cards_number > 2 and cards_number % 4 == 2:
                                # if int((cards_number - 2)/4) > 1:
                                # print(cards_number, int((cards_number - 2)/4))
                                wars.append(int((cards_number - 2)/4))
                                # wars.append(cards_number)
            if wins + looses > 0:
                print(wins + looses, "wins: ", wins / (wins + looses))
                if wins + looses in data:
                    data[wins+looses].append(wins / (wins + looses))
                else:
                    data[wins+looses] = [wins / (wins + looses)]

    end = time.time()
    print("time in sec", end - start)
    # print(sum(data[wins+looses]) / len(data[wins+looses]))
    if draw_box_plot:
        fig, ax = plt.subplots()
        ax.boxplot(np.array(list(data.values())), labels=[x * plays_in_range for x in range(1, ranges+1)])
        plt.show()
    if draw_turns_hist:
        fig, ax = plt.subplots()
        # decimal.getcontext().rounding = decimal.ROUND_UP
        ax.hist(turns_list, range=(0, int(math.floor(max(turns_list))/200)
                * 200 + 200), bins=int(math.floor(max(turns_list))/200 + 1))
        ax.yaxis.set_major_formatter(PercentFormatter(xmax=len(turns_list)))
        i = 0
        turns_dimension: dict[int, float] = {}
        while i < max(turns_list):
            tmp = [x for x in turns_list if x >= i and x < i + 200]
            turns_dimension[i + 200] = len(tmp) / len(turns_list) * 100
            i += 200
        print(turns_dimension)
        print("maksymalna liczba tur:", max(turns_list))
        plt.show()
    if draw_wars_hist:
        fig, ax = plt.subplots(1, 1, sharey=True, tight_layout=True)
        ax.hist(wars, bins=max(wars), range=(0.5, max(wars)+0.5))
        print(Counter(wars))
        plt.show()
