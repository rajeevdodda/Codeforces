# https://codeforces.com/contest/433/problem/B


def single_integer():
    return int(input())


def multi_integer():
    return map(int, input().split())


def string():
    return input()


def multi_string():
    return input().split()


n = single_integer()
integers = [0] + list(multi_integer())

sorted_integers = sorted(integers)
ans = 0
for i in range(n + 1):
    ans += sorted_integers[i]
    sorted_integers[i] = ans
ans = 0
for i in range(n + 1):
    ans += integers[i]
    integers[i] = ans

m = single_integer()

for i in range(m):
    t, l, r = multi_integer()
    if t == 2:
        print(sorted_integers[r] - sorted_integers[l - 1])
    else:
        print(integers[r] - integers[l - 1])
