# https://codeforces.com/contest/599/problem/A
def single_integer():
    return int(input())


def multi_integer():
    return map(int, input().split())


def string():
    return input()


def multi_string():
    return input().split()


d1, d2, d3 = multi_integer()

print(min(d1+d2+d3, 2*(d1+d2), 2*(d1+d3), 2*(d2+d3)))