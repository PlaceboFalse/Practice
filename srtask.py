import random
from typing import List


def default_sort(list_num: List[int]) -> None:
    for i in range(list_lenght):
        j = i + 1
        for j in range(list_lenght):
            if list_num[i] < list_num[j]:
                list_num[i], list_num[j] = list_num[j], list_num[i]


def quick_sort(list_to_sort: List[int]) -> List[int]:

    if len(list_to_sort) <= 1:
        return list_to_sort

    key = list_to_sort[0]

    left = list(filter(lambda x: x < key, list_to_sort))
    mid = list(filter(lambda x: x == key, list_to_sort))
    right = list(filter(lambda x: x > key, list_to_sort))

    return quick_sort(left) + mid + quick_sort(right)


if __name__ == '__main__':

    list_lenght = int(input())
    list_num = []

    for i in range(list_lenght):
        list_num.append(random.randint(0, min(1000, list_lenght * 2)))

    print(list_num)
    # default_sort(list_num)
    # print(list_num)
    print(quick_sort(list_num))
