# https://codeforces.com/problemset/problem/1428/A

for _ in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())

    if x1 == x2:
        print(abs(y1 - y2))
        pass
    elif y1 == y2:
        print(abs(x1 - x2))
    else:
        print(abs(x1 - x2) + abs(y1 - y2) + 2)
