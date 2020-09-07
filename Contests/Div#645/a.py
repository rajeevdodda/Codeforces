# https://codeforces.com/contest/1358/problem/0

def single_integer():
    return int(input())


def multi_integer():
    return map(int, input().split())


def string():
    return input()


def multi_string():
    return input().split()


t = single_integer()
for i in range(t):
    n, m = multi_integer()
    if n * m > max(n, m):
        if m % 2 == 0:
            print(n * (m // 2))
        else:
            print(n * (m // 2) + n // 2 + n % 2)
    elif n * m == max(n, m):
        max_value = max(n, m)
        min_value = min(n, m)
        print(max_value // 2 + max_value % 2)
