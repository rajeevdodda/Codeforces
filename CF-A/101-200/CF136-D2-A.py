# https://codeforces.com/contest/136/problem/A
n = int(input())
ans = [None] * n
gifts = map(int, input().split())

j = 1
for i in gifts:
    ans[i - 1] = j
    j += 1

print(*ans)
