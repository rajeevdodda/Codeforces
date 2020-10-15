# https://codeforces.com/problemset/problem/1255/A

for _ in range(int(input())):
    a, b = map(int, input().split())
    diff = abs(a - b)
    if diff % 5 == 0:
        print(diff // 5)
    elif diff % 5 == 1:
        print(diff // 5 + 1)
    elif diff % 5 == 2:
        print(diff // 5 + 1)
    elif diff % 5 == 3:
        print(diff // 5 + 2)
    elif diff % 5 == 4:
        print(diff // 5 + 2)
