# https://codeforces.com/problemset/problem/1368/A

for _ in range(int(input())):
    a, b, n = map(int, input().split())
    ans = 0
    if a > b:
        a, b = b, a

    while True:
        a += b
        ans += 1
        if a > n:
            print(ans)
            break

        b += a

        ans += 1
        if b > n:
            print(ans)
            break
