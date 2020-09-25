# https://codeforces.com/problemset/problem/1312/A

for _ in range(int(input())):
    n, m = map(int, input().split())
    if n % m == 0:
        print("YES")
    else:
        print("NO")