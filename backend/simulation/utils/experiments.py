import matplotlib.pyplot as plt
from simulation.game.game import Game
from simulation.game_config.configs import GameConfig, PlayerConfig, RulesConfig
from simulation.game_config.enums import CardsDistribution, DeckType, Strategy

def random_game_box_plot(samples: int, ranges: int, plays_in_range: int) -> None:
    data:dict[int, list[float]] = {}
    config = GameConfig(players=[PlayerConfig(Strategy.RANDOM_CARDS, None),
                        PlayerConfig(Strategy.RANDOM_CARDS, None)])
    for i in range(samples):       
        print('\n', i)      
        looses: int = 0
        wins: int = 0
        for _ in range(ranges):
            for _ in range(plays_in_range):
                game = Game(config)
                game.play()
                if game._players[0].num_cards == 0:
                    looses += 1
                else:
                    wins += 1
            print(wins + looses, "wins: ", wins / (wins + looses))
            if wins + looses in data:
                data[wins+looses].append(wins / (wins + looses))
            else:
                data[wins+looses] = [wins / (wins + looses)]
    fig, ax = plt.subplots()
    ax.boxplot(data.values(), labels=[x * plays_in_range for x in range(1, ranges + 1)])
    plt.show()
    
def balanced_deck_scenario(samples: int, ranges: int, plays_in_range: int, strategy: Strategy, draw_plot: bool=True) -> None:
    data:dict[int, list[float]] = {}
    config = GameConfig(
                            players=[
                                PlayerConfig(
                                    strategy, ['2S', '2C', '3S', '3C', '4S', '4C', '5S', '5C', '6S', '6C', '7S', '7C', '8S', '8C', '9S', '9C', 'TS', 'TC', 'JS', 'JC', 'QS', 'QC', 'KS', 'KC', 'AS', 'AC']
                                ),
                                PlayerConfig(
                                    Strategy.RANDOM_CARDS, 
                                    ['2H', '2D', '3H', '3D', '4H', '4D', '5H', '5D', '6H', '6D', '7H', '7D', '8H', '8D', '9H', '9D', 'TH', 'TD', 'JH', 'JD','QH', 'QD', 'KH', 'KD', 'AH', 'AD']
                                )
                            ],
                            cards_distribution=CardsDistribution.FIXED_RANDOM
                        )
    looses: int = 0
    wins: int = 0
    for i in range(samples):       
        print('\n', i)      
        looses = 0
        wins = 0
        for _ in range(ranges):
            for _ in range(plays_in_range):
                game = Game(config, debug=False)
                game.play()
                if game._players[0].num_cards == 0:
                    looses += 1
                else:
                    wins += 1
            print(wins + looses, "wins: ", wins / (wins + looses))
            if wins + looses in data:
                data[wins+looses].append(wins / (wins + looses))
            else:
                data[wins+looses] = [wins / (wins + looses)]
    print(sum(data[wins+looses]) / len(data[wins+looses]))
    if draw_plot:
        fig, ax = plt.subplots()
        ax.boxplot(data.values(), labels=[x * 1000 for x in range(1, 2)])
        plt.show()

