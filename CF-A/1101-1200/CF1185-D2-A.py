# https://codeforces.com/problemset/problem/1185/A

a, b, c, d = map(int, input().split())

l = sorted([a, b, c])
ans = 0
if l[1] - l[0] < d:
    ans += (d - l[1] + l[0])

if l[2] - l[1] < d:
    ans += (d - l[2] + l[1])
print(ans)