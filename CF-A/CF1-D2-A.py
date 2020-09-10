# https://codeforces.com/contest/1/problem/A
import math

m, n, a = map(int, input().split())

print((math.ceil(m/a) * (math.ceil(n/a))))
