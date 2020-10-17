# https://codeforces.com/problemset/problem/1315/A

for _ in range(int(input())):
    a, b, x, y = map(int, input().split())
    bottom = a * (b - y - 1)
    top = a * y
    right = b * (a - x - 1)
    left = b * x
    print(max(top, bottom, left, right))
