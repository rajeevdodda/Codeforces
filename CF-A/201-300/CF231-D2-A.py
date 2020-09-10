# https://codeforces.com/contest/231/problem/A

n = int(input())
ans = 0
for i in range(n):
    problems = map(int, input().split())
    if sum(problems) >= 2:
        ans += 1

print(ans)
