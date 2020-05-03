# https://codeforces.com/contest/723/problem/A
points = tuple(map(int, input().split()))

print(max(points) - min(points))