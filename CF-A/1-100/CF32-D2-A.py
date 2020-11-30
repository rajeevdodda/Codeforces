# https://codeforces.com/problemset/problem/32/A

n, d = map(int, input().split())

soldiers = tuple(map(int, input().split()))
ans = 0
for i in range(n):
    for j in range(n):
        if i != j and abs(soldiers[i] - soldiers[j]) <= d:
            ans += 1

print(ans)
