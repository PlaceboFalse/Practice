from typing import List
from srtask import quick_sort


def coin(Number: int) -> List[int]:

    coin: tuple = (1, 5, 10, 25, 50, 100)
    list_coin: List[int] = []
    list_coin.append(coin[0])

    return list_coin


if __name__ == "__main__":
    Number: int = int(input())

    print(quick_sort(coin(Number)))
