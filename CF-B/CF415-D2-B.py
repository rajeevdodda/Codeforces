# https://codeforces.com/contest/415/problem/B


def single_integer():
    return int(input())


def multi_integer():
    return map(int, input().split())


def string():
    return input()


def multi_string():
    return input().split()


import math

n, a, b = multi_integer()
tokens = multi_integer()

for i in tokens:
    x = (i * a) // b
    k = i - math.ceil((x * b) / a)

    print(k, end=" ")
