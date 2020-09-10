# https://codeforces.com/contest/799/problem/A
import math

n, t, k, d = map(int, input().split())

total_time = (math.ceil(n / k)) * t

if total_time - t > d:
    print("Yes")
else:
    print("No")


