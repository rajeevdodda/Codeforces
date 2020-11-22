# https://codeforces.com/problemset/problem/669/A

n = int(input())

x = n // 3
if n % 3 == 0:
    print(x * 2)
else:
    print(x * 2 + 1)