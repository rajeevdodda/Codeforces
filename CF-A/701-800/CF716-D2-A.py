# https://codeforces.com/problemset/problem/716/A

n, c = map(int, input().split())

t = tuple(map(int, input().split()))
ans = 0
for i in range(1, n):
    if t[i] - t[i-1] > c:
        ans = 0
    else:
        ans += 1

print(ans+1)