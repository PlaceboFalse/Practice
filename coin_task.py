from typing import List


def coin(Number: int) -> List[int]:

    coin: tuple = (1, 5, 10, 25, 50, 100)
    answer_coin: List[int] = []
    answer_coin.append(coin[0])
    return answer_coin


Number: int = int(input())

print(coin(Number))
