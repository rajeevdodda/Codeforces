# https://codeforces.com/contest/272/problem/A


def single_integer():
    return int(input())


def multi_integer():
    return map(int, input().split())


def string():
    return input()


def multi_string():
    return input().split()


n = single_integer()
total = sum(multi_integer())
ans = 0

i = 1

while i < 6:
    if (total + i) % (n + 1) != 1:
        ans += 1
    i += 1

print(ans)
