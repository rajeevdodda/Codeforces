# https://codeforces.com/problemset/problem/1437/A

for _ in range(int(input())):
    l, r = map(int, input().split())

    if 2 * l > r:
        print("YES")
    else:
        print("NO")