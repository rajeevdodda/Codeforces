# https://codeforces.com/problemset/problem/780/A

n = input()

s = set()
ans = 0


for i in input().split():
    if i not in s:
        s.add(i)
        ans = max(ans, len(s))
    else:
        s.discard(i)
print(ans)