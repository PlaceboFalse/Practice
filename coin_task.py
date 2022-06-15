from typing import List, Any
from srtask import quick_sort


def find_coin(Number: int) -> Any:

    start_coin: tuple = (100, 25, 10, 5, 1)
    list_coin: List[int] = []

    if Number < 1:
        return 0

    while Number != 0:
        for i in range(5):
            if Number - start_coin[i] >= 0:
                list_coin.append(start_coin[i])
                Number -= start_coin[i]
                break

    return quick_sort(list_coin)


if __name__ == "__main__":

    Number: int = int(input())

    if find_coin(Number) == 0:
        print("Can't finde coin")
    else:
        print(find_coin(Number))
