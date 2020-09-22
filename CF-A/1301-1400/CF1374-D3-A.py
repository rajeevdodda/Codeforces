# https://codeforces.com/problemset/problem/1374/A

t = int(input())

for i in range(t):
    x, y, n = map(int, input().split())
    b = n % x
    if b == y:
        print(n)
    elif b < y:
        print(n - b - (x -y))
    else:
        print(n - b + y)