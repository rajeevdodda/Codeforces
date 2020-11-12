# https://codeforces.com/problemset/problem/1443/A

for _ in range(int(input())):
    n = int(input())

    for i in range(n):
        print(4*n - i*2, end=" ")
    print()
