# https://codeforces.com/problemset/problem/1075/A

n = int(input())

x, y = map(int, input().split())

if x + y - 2 <= n + n - x - y:
    print("White")
else:
    print("Black")
