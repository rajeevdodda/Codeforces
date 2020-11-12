# https://codeforces.com/problemset/problem/1413/A

for _ in range(int(input())):
    n = int(input())
    a = tuple(map(int, input().split()))

    for i in range(0, n, 2):
        #if a[i] < 0 and a[i + 1] < 0 or a[i] > 0 and a[i + 1] > 0:
        print(-1 * a[i + 1], a[i], end=" ")

    print()

