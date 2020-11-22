# https://codeforces.com/problemset/problem/760/A

import math

m, d = map(int, input().split())
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

a = math.ceil((months[m - 1] - (7 - d + 1)) / 7)
print(a + 1)
