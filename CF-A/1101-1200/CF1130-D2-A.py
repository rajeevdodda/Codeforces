# https://codeforces.com/problemset/problem/1130/A
import math

n = int(input())

positive = negative = zero = 0

for i in map(int, input().split()):
    if i == 0:
        zero += 1
    elif i > 0:
        positive += 1
    else:
        negative += 1

if positive >= math.ceil(n / 2) or negative >= math.ceil(n / 2):
    if positive > negative:
        print(1)
    else:
        print(-1)
else:
    print(0)

