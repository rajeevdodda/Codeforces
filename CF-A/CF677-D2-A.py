# https://codeforces.com/contest/677/problem/A

n, h = map(int, input().split())
a = list(map(int, input().split()))
width = 0
for i in a:
    if i % h == 0:
        width += i // h
    else:
        width += i // h + 1
print(width)