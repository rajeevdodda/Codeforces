# https://codeforces.com/contest/460/problem/A


def single_integer():
    return int(input())


def multi_integer():
    return map(int, input().split())


def string():
    return input()


def multi_string():
    return input().split()


n, m = multi_integer()
ans = 0
while True:
    if n >= m:
        n = n - m + 1
        ans += m
    else:
        ans += n
        break

print(ans)
