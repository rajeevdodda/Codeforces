# https://codeforces.com/contest/268/problem/A

n = int(input())
home = dict()
away = dict()
ans = 0
for i in range(n):
    h, a = input().split()
    if h not in home:
        home[h] = home.get(h, 0) + 1
    else:
        home[h] = home.get(h) + 1
    if a not in away:
        away[a] = away.get(a, 0) + 1
    else:
        away[a] = away.get(a) + 1
    if h in away:
        ans += away[h]
    if a in home:
        ans += home[a]

print(ans)
