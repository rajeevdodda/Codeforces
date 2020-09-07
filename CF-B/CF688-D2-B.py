# https://codeforces.com/contest/688/problem/B


def single_integer():
    return int(input())


def multi_integer():
    return map(int, input().split())


def string():
    return input()


def multi_string():
    return input().split()


s = string()

print(s + s[::-1])