# https://codeforces.com/problemset/problem/1392/B

for _ in range(int(input())):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))

    a_max = float('-inf')
    a_min = float('inf')

    for i in range(n):
        if a[i] > a_max:
            a_max = a[i]
        if a[i] < a_min:
            a_min = a[i]

    for k in range(n):
        a[k] = a_max - a[k]

    if x % 2 == 0:
        for k in range(n):
            a[k] = a_max - a_min - a[k]

    print(*a)