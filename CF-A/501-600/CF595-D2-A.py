# https://codeforces.com/problemset/problem/595/A

n, m = map(int, input().split())
ans = 0
for i in range(n):
    floor = tuple(input().split())
    for k in range(0, 2 * m, 2):
        if floor[k] == '1' or floor[k + 1] == '1':
            ans += 1

print(ans)