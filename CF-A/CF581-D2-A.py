# https://codeforces.com/contest/581/problem/A

r, b = map(int, input().split())

print(min(r, b), abs(r - b) // 2)
