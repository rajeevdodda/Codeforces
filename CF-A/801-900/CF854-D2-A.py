# https://codeforces.com/problemset/problem/854/A
from math import gcd

n = int(input())

if n % 2 == 0:
    a, b = n // 2 - 1, n // 2 + 1
else:
    a, b = n // 2, n // 2 + 1

while gcd(a, b) != 1:
    a -= 1
    b += 1

print(a, b)
