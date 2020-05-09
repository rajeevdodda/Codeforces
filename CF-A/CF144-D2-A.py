# https://codeforces.com/contest/144/problem/A


def single_integer():
    return int(input())


def multi_integer():
    return map(int, input().split())


def string():
    return input()


def multi_string():
    return input().split()


n = single_integer()
soldiers = tuple(multi_integer())

i, j = 0, n - 1
high = float('-inf')
low = float('inf')
high_index = low_index = None
while i < n:
    if soldiers[i] > high:
        high, high_index = soldiers[i], i

    if soldiers[i] <= low:
        low = soldiers[i]
        low_index = i
    i += 1

if high_index < low_index:
    print(high_index + (n - 1 - low_index))
else:
    print(high_index + (n - 1 - low_index) - 1)
