# https://codeforces.com/problemset/problem/884/A

n, t = map(int, input().split())

days = map(int, input().split())

ans = 1
for i in days:
    if t <= 86400 - i:
        print(ans)
        break
    else:
        t -= (86400 - i)
        ans += 1