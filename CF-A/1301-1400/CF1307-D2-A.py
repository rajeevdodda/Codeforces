# https://codeforces.com/problemset/problem/1307/A

for _ in range(int(input())):
    n, d = map(int, input().split())
    haybales = tuple(map(int, input().split()))
    ans = haybales[0]
    for i in range(1, n):
        if d > 0:
            x = min(haybales[i], d // i)
            ans += x
            d -= (x * i)
        else:
            break
    print(ans)
