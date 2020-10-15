# https://codeforces.com/problemset/problem/919/A

n, m = map(int, input().split())

min_value = float('inf')

for i in range(n):
    a, b = map(int, input().split())
    min_value = min(min_value, a/b)

print(min_value*m)