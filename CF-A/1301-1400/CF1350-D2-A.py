# https://codeforces.com/problemset/problem/1350/A

for _ in range(int(input())):
    n, k = map(int, input().split())

    for i in range(2, n + 1):
        if n % i == 0:
            n += i
            break

    print(n + 2 * (k - 1))
