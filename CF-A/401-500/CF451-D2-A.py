# https://codeforces.com/contest/451/problem/A


def single_integer():
    return int(input())


def multi_integer():
    return map(int, input().split())


def string():
    return input()


def multi_string():
    return input().split()


n, m = multi_integer()

if m <= n:
    temp = m
else:
    temp = n

if temp % 2 == 0:
    print("Malvika")
else:
    print("Akshat")
