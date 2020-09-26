# https://codeforces.com/problemset/problem/448/A

import math

cups = sum(map(int, input().split()))
medals = sum(map(int, input().split()))

shelves = int(input())
if math.ceil(cups / 5) + math.ceil(medals / 10) > shelves:
    print("NO")
else:
    print("YES")
