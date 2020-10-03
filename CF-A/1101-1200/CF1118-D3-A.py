# https://codeforces.com/problemset/problem/1118/A

for _ in range(int(input())):
    n, a, b = map(int, input().split())
    if n == 1:
        print(a)
    else:
        if b / 2 > a:
            print(n * a)
        else:
            print((n // 2) * b + (n % 2) * a)
