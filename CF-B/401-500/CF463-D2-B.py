# https://codeforces.com/contest/463/problem/B


def single_integer():
    return int(input())


def multi_integer():
    return map(int, input().split())


def string():
    return input()


def multi_string():
    return input().split()


n = single_integer()
pylons_list = multi_integer()

pylon_height = 0
energy = 0
dollars = 0

for i in pylons_list:
    if (pylon_height + energy) <= i:
        dollars += (i - (pylon_height + energy))
        pylon_height = i
        energy = 0
    else:
        energy += (pylon_height - i)
        pylon_height = i

print(dollars)
