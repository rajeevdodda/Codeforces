# https://codeforces.com/problemset/problem/1077/A

for _ in range(int(input())):
    a, b, k = map(int, input().split())

    print((a - b) * (k // 2) + (a * (k % 2)))
