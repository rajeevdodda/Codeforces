# https://codeforces.com/problemset/problem/1294/A

t = int(input())

for i in range(t):
    a, b, c, n = map(int, input().split())
    max_coin = max(a, b, c)

    final = a + b + c + n
    if final % 3 == 0 and final / 3 >= max_coin:
        print("YES")
    else:
        print("NO")
