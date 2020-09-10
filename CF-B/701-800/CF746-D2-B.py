# https://codeforces.com/contest/746/problem/B


def single_integer():
    return int(input())


def multi_integer():
    return map(int, input().split())


def string():
    return input()


def multi_string():
    return input().split()


n = single_integer()
s = string()
ans = ""

while s:

    if len(s) % 2 == 0:
        ans = s[0] + ans
    else:
        ans = ans + s[0]
    if len(s) == 1:
        break
    else:
        s = s[1:]

print(ans)
