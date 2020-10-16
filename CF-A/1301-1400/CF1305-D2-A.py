# https://codeforces.com/problemset/problem/1305/A

for _ in range(int(input())):
    n = input()
    a = sorted(map(int, input().split()))
    b = sorted(map(int, input().split()))
    print(*a)
    print(*b)
