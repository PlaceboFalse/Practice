import random


def defaultsort():
    for i in range(n):
        j = i + 1
        for j in range(n):
            if a[i] < a[j]:
                a[i], a[j] = a[j], a[i]


def quicksort(number):

    if len(number) <= 1:
        return number

    elements = number[0]
    left = list(filter(lambda x: x < elements, number))
    mid = [i for i in number if i == elements]
    right = list(filter(lambda x: x > elements, number))
    return quicksort(left) + mid + quicksort(right)


n = int(input())
a = []
for i in range(n):
    a.append(random.randint(0, min(1000, n * 2)))

print(a)
defaultsort()
# print(quicksort(a))
print(a)
