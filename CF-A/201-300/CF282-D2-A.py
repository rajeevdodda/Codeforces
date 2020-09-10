# https://codeforces.com/contest/282/problem/A

n = int(input())

ans = 0

for i in range(n):
    if '++' in input():
        ans += 1
    else:
        ans -= 1

print(ans)