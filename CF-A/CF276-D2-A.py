# https://codeforces.com/contest/276/problem/A


def single_integer():
    return int(input())


def multi_integer():
    return map(int, input().split())


def string():
    return input()


def multi_string():
    return input().split()


n, k = multi_integer()

ans = float('-inf')

for i in range(n):
    f, t = multi_integer()
    if k > t:
        ans = max(f, ans)
    else:
        temp = f - (t - k)
        ans = max(temp, ans)


print(ans)
