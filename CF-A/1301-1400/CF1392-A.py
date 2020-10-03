# https://codeforces.com/problemset/problem/1392/A

for _ in range(int(input())):
    n = input()
    if len(set(input().split())) == 1:
        print(n)
    else:
        print(1)