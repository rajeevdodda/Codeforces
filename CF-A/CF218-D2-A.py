# http://codeforces.com/contest/218/problem/A

n, k = map(int, input().split())

points = list(map(int, input().split()))

for j in range(1, len(points), 2):
    if k > 0:
        if points[j - 1] < points[j] - 1 > points[j + 1]:
            points[j] = points[j] - 1
            k -= 1
print(*points)
