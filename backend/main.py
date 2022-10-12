from strategy.test import Test


def main(test_str: str) -> None:
    card = Test()
    print(card.hello() + ' ' + test_str)


if __name__ == "__main__":
    main('Test')
