# https://codeforces.com/contest/318/problem/A
import math
n, k = map(int, input().split())

if k <= math.ceil(n/2):
    print(1 + (k - 1) * 2)
else:
    k = (k - math.ceil(n/2))
    print(2 + (k - 1) * 2)
