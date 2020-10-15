# https://codeforces.com/problemset/problem/984/A

n = int(input())
a = sorted(map(int, input().split()), reverse=True)

print(a[n//2])