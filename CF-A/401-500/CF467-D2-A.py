# https://codeforces.com/contest/467/problem/A

n = int(input())
ans = 0
for i in range(n):
    p, q = map(int, input().split())
    if q - p >= 2:
        ans +=1

print(ans)
