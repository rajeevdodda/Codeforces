# https://codeforces.com/contest/451/problem/B


def single_integer():
    return int(input())


def multi_integer():
    return map(int, input().split())


def string():
    return input()


def multi_string():
    return input().split()


n = single_integer()
numbers = list(multi_integer())
new_list = list()
count = 0
