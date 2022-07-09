"make list"
import random
from typing import List


class SortedList:
    "Class for sorted lists"
    @staticmethod
    def default_sort(list_num: List[int]) -> None:
        "sort list."

        for i in range(list_lenght):
            j = i + 1
            for j in range(list_lenght):
                if list_num[i] < list_num[j]:
                    list_num[i], list_num[j] = list_num[j], list_num[i]

    @staticmethod
    def quick_sort(list_to_sort: List[int]) -> List[int]:
        "quick_sort list"
        if len(list_to_sort) <= 1:
            return list_to_sort

        key = list_to_sort[0]

        left = list(filter(lambda x: x < key, list_to_sort))
        mid = list(filter(lambda x: x == key, list_to_sort))
        right = list(filter(lambda x: x > key, list_to_sort))

        return SortedList.quick_sort(left) + mid + SortedList.quick_sort(right)


if __name__ == '__main__':

    list_lenght = int(input())
    list_num_begins = []
    for start in range(list_lenght):
        list_num_begins.append(random.randint(0, min(1000, list_lenght * 2)))

    print(list_num_begins)
    # default_sort(list_num_begins)
    # print(list_num_begins)
    print(SortedList.quick_sort(list_num_begins))
