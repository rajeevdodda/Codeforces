# https://codeforces.com/problemset/problem/1009/A

n, m = map(int, input().split())

c = tuple(map(int, input().split()))
a = tuple(map(int, input().split()))

i = j = 0
ans = 0
while i < n and j < m:
    if c[i] <= a[j]:
        ans += 1
        i += 1
        j += 1
    else:
        i += 1
print(ans)
