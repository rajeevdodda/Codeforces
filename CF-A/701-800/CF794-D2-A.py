# https://codeforces.com/problemset/problem/794/A

a, b, c = map(int, input().split())

n = int(input())
ans = 0
for i in map(int, input().split()):
    if b < i < c:
        ans += 1
print(ans)