# https://codeforces.com/problemset/problem/965/A

import math
k, n, s, p = map(int, input().split())

print(math.ceil(k * math.ceil(n/s)/ p))
