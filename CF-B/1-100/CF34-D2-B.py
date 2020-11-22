# https://codeforces.com/problemset/problem/34/B

n, m = input().split()

tv = sorted(map(int, input().split()))
ans = 0
for i in range(int(m)):
    if tv[i]< 0:
        ans += tv[i]
    else:
        break

print(-1*ans)
