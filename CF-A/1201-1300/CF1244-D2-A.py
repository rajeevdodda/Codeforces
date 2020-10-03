# https://codeforces.com/problemset/problem/1244/A
import math

for _ in range(int(input())):
    a, b, c, d, k = map(int, input().split())
    x = math.ceil(a / c)
    y = math.ceil(b / d)

    if x + y > k:
        print(-1)
    else:
        if x > y:
            print(x, k - x)
        else:
            print(k-y, y)