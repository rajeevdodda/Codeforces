# https://codeforces.com/problemset/problem/1243/A

for _ in range(int(input())):
    n = int(input())
    planks = sorted(map(int, input().split()))
    ans = 0

    for i in range(n):
        ans = max(ans, min(planks[i], (n - i)))
    print(ans)
