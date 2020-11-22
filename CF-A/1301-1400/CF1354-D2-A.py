# https://codeforces.com/problemset/problem/1354/A
import math
for _ in range(int(input())):
    a, b, c, d = map(int, input().split())

    if a <= b:
        print(b)
    else:
        slept = b
        if c <= d:
            print(-1)
        else:
            diff = c - d
            sleep_needed = a - b
            print(b + math.ceil(sleep_needed/diff) * c)



