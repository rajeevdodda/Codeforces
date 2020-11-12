# https://codeforces.com/problemset/problem/908/A

ans = 0
for i in input():
    s = set('aeiou13579')

    if i in s:
        ans += 1

print(ans)
