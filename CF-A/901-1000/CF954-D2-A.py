# https://codeforces.com/problemset/problem/954/A

n = int(input())

s = input()

ans = 0
i = 1
while i < n:
    if s[i-1] != s[i]:
        ans += 1
        i += 2
    else:
        i += 1

print(n - ans)