# https://codeforces.com/problemset/problem/796/A

n, m, k = map(int, input().split())

houses = tuple(map(int, input().split()))

min_distance = float('inf')

for i in range(n):
    if houses[i] == 0:
        continue
    if i == m - 1:
        continue

    if houses[i] <= k:
        min_distance = min(min_distance, abs(m - 1 - i))
print(min_distance*10)
