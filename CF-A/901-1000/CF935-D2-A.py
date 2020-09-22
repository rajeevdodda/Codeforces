# https://codeforces.com/problemset/problem/935/A

n = int(input())

ans = 0
i = 1
while i <= n // 2:
    if n % i == 0:
        ans += 1
    i += 1

print(ans)
