# https://codeforces.com/contest/588/problem/A


def single_integer():
    return int(input())


def multi_integer():
    return map(int, input().split())


def string():
    return input()


def multi_string():
    return input().split()


n = single_integer()
ans = 0
previous = float('inf')
for i in range(1, n + 1):
    a, p = multi_integer()
    if p > previous:
        ans += a * previous
    else:
        ans += a * p
        previous = p

print(ans)
