# https://codeforces.com/problemset/problem/851/A

n, k, t = map(int, input().split())

if t <= k:
    print(t)
elif t <= n:
    print(k)
else:
    print(n + k - t)
