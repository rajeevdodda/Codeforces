# https://codeforces.com/problemset/problem/1148/A

a, b, c = map(int, input().split())

if a > b:
    print(2 * (c + b) + 1)
elif a == b:
    print(2 * (a + c))
else:
    print(2 * (a + c) + 1)
