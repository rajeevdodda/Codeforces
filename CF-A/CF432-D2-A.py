# https://codeforces.com/contest/432/problem/A


def single_integer():
    return int(input())


def multi_integer():
    return map(int, input().split())


def string():
    return input()


def multi_string():
    return input().split()


n, k = multi_integer()

shows = multi_integer()
ans = 0

for i in shows:
    if i + k <= 5:
        ans += 1

print(ans//3)
