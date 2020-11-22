# https://codeforces.com/problemset/problem/859/A

k = int(input())

contestants = tuple(map(int, input().split()))

max_contestant = max(contestants)

if max_contestant <= 25:
    print(0)
else:
    print(max_contestant - 25)