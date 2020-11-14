# https://codeforces.com/problemset/problem/931/A

a = int(input())
b = int(input())

x = abs(a - b) // 2

if abs(a - b) % 2 == 0:
    print(x * (x + 1))
else:
    print(x * (x + 1) + x + 1)
