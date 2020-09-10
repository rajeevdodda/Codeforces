# https://codeforces.com/contest/214/problem/A


def single_integer():
    return int(input())


def multi_integer():
    return map(int, input().split())


def string():
    return input()


def multi_string():
    return input().split()


ans_set = set()

n, m = multi_integer()

a = 0
while True:
    b = n - (a ** 2)
    if b >= 0:
        if a + (b ** 2) == m:
            ans_set.add((a, b))
            a += 1
        else:
            a += 1
    else:
        break

print(len(ans_set))

