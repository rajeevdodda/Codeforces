# https://codeforces.com/contest/148/problem/A


def single_integer():
    return int(input())


def multi_integer():
    return map(int, input().split())


def string():
    return input()


def multi_string():
    return input().split()


k = single_integer()
l = single_integer()
m = single_integer()
n = single_integer()
d = single_integer()

ans = 0
if k == 1 or l == 1 or m == 1 or n == 1:
    print(d)
else:
    for i in range(1, d + 1):
        if i % k == 0 or i % l == 0 or i % m == 0 or i % n == 0:
            ans += 1
    print(ans)