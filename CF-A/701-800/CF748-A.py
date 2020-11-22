# https://codeforces.com/problemset/problem/748/A
import math

n, m, k = map(int, input().split())

lane = math.ceil(k / (2 * m))

desk = math.ceil((k - (2 * m * (lane - 1))) / 2)

if k % 2 == 0:
    print(lane, desk, "R")
else:
    print(lane, desk, "L")
