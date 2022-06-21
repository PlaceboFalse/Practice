from typing import List, Any
from srtask import quick_sort


class Searching():

    @staticmethod
    def amount_in_coin(amount: int) -> Any:
        if amount < 1:
            return 0

        coins: tuple = (100, 25, 10, 5, 1)
        list_coin: List[int] = []

        while amount != 0:
            for i in range(len(coins)):
                if amount - coins[i] >= 0:
                    list_coin.append(coins[i])
                    amount -= coins[i]
                    break

        return quick_sort(list_coin)


if __name__ == "__main__":

    amount: int = int(input())

    if Searching.amount_in_coin(amount) == 0:
        print("Can't finde coin")
    else:
        print(Searching.amount_in_coin(amount))
