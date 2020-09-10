# https://codeforces.com/contest/50/problem/A

n, m = map(int, input().split())

if m % 2 == 0:
    print( n * ( m // 2))
else:
    print( n * ( m // 2) + (n//2))