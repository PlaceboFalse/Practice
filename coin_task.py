"Check typing and sort"
from typing import List, Any
from srtask import SortedList


class Searching():
    "Class for found coin"

    @staticmethod
    def nothing():
        "Nothing"

    @staticmethod
    def amount_in_coin(amount: int) -> Any:
        "found coin"
        if amount < 1:
            return 0

        coins: tuple = (100, 25, 10, 5, 1)
        list_coin: List[int] = []

        while amount != 0:
            for i in enumerate(coins):
                if amount - i[1] >= 0:
                    list_coin.append(i[1])
                    amount -= i[1]
                    break

        return SortedList.quick_sort(list_coin)


if __name__ == "__main__":

    amount_begin: int = int(input())

    if Searching.amount_in_coin(amount_begin) == 0:
        print("Can't finde coin")
    else:
        print(Searching.amount_in_coin(amount_begin))
