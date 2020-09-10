# https://codeforces.com/contest/766/problem/B


def single_integer():
    return int(input())


def multi_integer():
    return map(int, input().split())


def string():
    return input()


def multi_string():
    return input().split()


n = single_integer()

lines = list(multi_integer())
lines.sort()
ans = False
i = 0
j = n - 2
k = n - 1

for i in range(n - 2):
    if lines[i] + lines[i + 1] > lines[i + 2]:
        print("YES")
        break
else:
    print("NO")
