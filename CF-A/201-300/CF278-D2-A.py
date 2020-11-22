# https://codeforces.com/problemset/problem/278/A


_ = input()
distances = tuple(map(int, input().split()))
a, b = map(int, input().split())
a, b = min(a, b), max(a, b)
front = sum(distances[a-1: b-1])
back = 0
total = sum(distances)
if front < total - front:
    print(front)
else:
    print(total-front)

