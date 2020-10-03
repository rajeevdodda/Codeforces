# https://codeforces.com/problemset/problem/1180/A
ans = 1
n = int(input())

if n == 1:
    print(ans)
else:
    for i in range(2, n + 1):
        ans += 4 * (i - 1)

    print(ans)
