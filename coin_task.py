from typing import List
from srtask import quick_sort


def find_coin(Number: int) -> List[int]:

    start_coin: tuple = (100, 25, 10, 5, 1)
    list_coin: List[int] = []

    while Number != 0:
        for i in range(5):
            if Number - start_coin[i] >= 0:
                list_coin.append(start_coin[i])
                Number -= start_coin[i]

    return list_coin


if __name__ == "__main__":
    Number: int = int(input())
    if Number < 1:
        print("can't finde coin")
    else:
        print(quick_sort(find_coin(Number)))
