# https://codeforces.com/problemset/problem/38/A

n = int(input())
ranks = tuple(map(int, input().split()))

a, b = map(int, input().split())

ans = 0
for i in range(a-1, b-1):
    ans += ranks[i]
print(ans)