# https://codeforces.com/problemset/problem/1391/B

for _ in range(int(input())):

    n, m = map(int, input().split())
    ans = 0
    for i in range(n - 1):
        if input()[-1] == "R":
            ans += 1

    for i in input():
        if i == "D":
            ans += 1

    print(ans)
