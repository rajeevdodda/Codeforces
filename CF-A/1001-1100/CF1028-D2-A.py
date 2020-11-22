# https://codeforces.com/problemset/problem/1028/A

n, m = map(int, input().split())

a, b = None, None

for i in range(n):
    side = input()
    for k in range(m):
        if side[k] == 'B':
            a = k + 1
            break
    if a is not None:
        for k in range(m - 1, -1, -1):
            if side[k] == 'B':
                b = k + 1
                break
    if a is not None and b is not None:
        length = b - a
        print(i + 1 + length // 2, (b + a) // 2)
        break
