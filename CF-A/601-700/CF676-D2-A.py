# https://codeforces.com/contest/676/problem/A


def single_integer():
    return int(input())


def multi_integer():
    return map(int, input().split())


def string():
    return input()


def multi_string():
    return input().split()


n = single_integer()
permutation = tuple(multi_integer())
i = 1
max_value = min_value = permutation[0]
max_index = min_index = 1

while i < n:
    if permutation[i] > max_value:
        max_index, max_value = i + 1, permutation[i]

    if permutation[i] < min_value:
        min_index, min_value = i + 1, permutation[i]

    i += 1

print(max(abs(n - max_index), abs(n - min_index), abs(1 - max_index), abs(1 - min_index)))
