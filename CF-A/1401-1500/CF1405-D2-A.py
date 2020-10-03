# https://codeforces.com/problemset/problem/1405/A


for _ in range(int(input())):
    n = input()
    l = list(map(int, input().split()))
    print(*l[::-1])
