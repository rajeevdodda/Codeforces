# https://codeforces.com/problemset/problem/1031/A

w, h, k = map(int, input().split())

ans = 0
while k > 0:
    ans += 2 * (w + h - 2)
    w -= 4
    h -= 4
    k -= 1
print(ans)
