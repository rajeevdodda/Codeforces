# https://codeforces.com/problemset/problem/1096/A

n = int(input())

for i in range(n):
    l, r = map(int, input().split())
    print(l, l + l)