from strategy.test import Test
from strategy.testClass import Test2


def main(test_str: str) -> None:
    card = Test()
    print(card.hello() + ' ' + test_str)
    card2 = Test2()
    


if __name__ == "__main__":
    main('Test')
