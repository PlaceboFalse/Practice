from typing import List
from srtask import quick_sort


def find_coin(Number: int) -> List[int]:

    start_coin: tuple = (1, 5, 10, 25, 100)
    list_coin: List[int] = []

    while Number > 0:
        if Number - start_coin[4] >= 0:
            Number -= start_coin[4]
            list_coin.append(start_coin[4])
        elif Number - start_coin[3] >= 0:
            Number -= start_coin[3]
            list_coin.append(start_coin[3])
        elif Number - start_coin[2] >= 0:
            Number -= start_coin[2]
            list_coin.append(start_coin[2])
        elif Number - start_coin[1] >= 0:
            Number -= start_coin[1]
            list_coin.append(start_coin[1])
        else:
            Number -= start_coin[0]
            list_coin.append(start_coin[0])

    return list_coin


if __name__ == "__main__":
    Number: int = int(input())
    if Number < 1:
        print("can't finde coin")
    else:
        print(quick_sort(find_coin(Number)))
