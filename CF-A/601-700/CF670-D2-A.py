# https://codeforces.com/contest/670/problem/A


def single_integer():
    return int(input())


def multi_integer():
    return map(int, input().split())


def string():
    return input()


def multi_string():
    return input().split()


n = single_integer()
ans = (n // 7) * 2
if n % 7 == 0:
    print(ans, ans)
else:
    if n % 7 == 1:
        print(ans, ans + 1)
    elif n % 7 == 6:
        print(ans+1, ans + 2)
    else:
        print(ans, ans + 2)
