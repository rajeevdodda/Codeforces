# https://codeforces.com/problemset/problem/1099/A

w, h = map(int, input().split())
u1, d1 = map(int, input().split())
u2, d2 = map(int, input().split())

while h > 0:
    w += h
    if d1 == h:
        w = max(w - u1, 0)
    if d2 == h:
        w = max(w - u2, 0)
    h -= 1


print(w)