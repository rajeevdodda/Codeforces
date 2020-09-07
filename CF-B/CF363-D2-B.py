# https://codeforces.com/contest/363/problem/B


def single_integer():
    return int(input())


def multi_integer():
    return map(int, input().split())


def string():
    return input()


def multi_string():
    return input().split()


from collections import deque

n, k = multi_integer()
d = deque()
fence = tuple(multi_integer())
min_sum = 0

for i in range(k):
    min_sum += fence[i]
    d.append((fence[i], i + 1))

min_index = 1
width_sum = min_sum

for i in range(k, n):
    left_element, left_index = d.popleft()
    width_sum = width_sum - left_element + fence[i]
    if width_sum <= min_sum:
        min_sum = width_sum
        min_index = left_index + 1
    d.append((fence[i], i + 1))


print(min_index)
