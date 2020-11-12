# https://codeforces.com/problemset/problem/1436/A

for _ in range(int(input())):
    n, m = input().split()
    if sum(map(int, input().split())) == int(m):
        print("YES")
    else:
        print("NO")