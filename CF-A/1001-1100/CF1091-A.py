# https://codeforces.com/problemset/problem/1091/A


y, b, r = map(int, input().split())

print(min(y+2, b+1, r)*3 -3)
