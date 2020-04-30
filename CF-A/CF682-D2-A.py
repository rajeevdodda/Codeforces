# https://codeforces.com/contest/682/problem/A

n, m = map(int, input().split())

ans = 0
i = 1

while i <= n:
    ans += (m + (i % 5)) // 5
    i += 1

print(ans)
