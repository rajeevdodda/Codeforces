# https://codeforces.com/problemset/problem/1234/A
import math

for _ in range(int(input())):
    n = int(input())
    ans = math.ceil(sum(map(int, input().split())) / n)
    print(ans)
