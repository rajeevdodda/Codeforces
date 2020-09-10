# https://codeforces.com/contest/492/problem/A


def single_integer():
    return int(input())


def multi_integer():
    return map(int, input().split())


def string():
    return input()


def multi_string():
    return input().split()


n = single_integer()
i = 1
ans = 0
while True:
    ans += i * (i + 1) // 2
    if ans == n:
        print(i)
        break
    elif ans > n:
        print(i - 1)
        break

    i += 1

