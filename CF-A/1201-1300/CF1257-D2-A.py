# https://codeforces.com/problemset/problem/1257/A

for _ in range(int(input())):
    n, x, a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    diff = a - 1 + n - b
    if diff > x:
        print(b - a + x)
    else:
        print(n - 1)
