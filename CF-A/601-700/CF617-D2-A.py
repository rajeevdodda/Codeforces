# https://codeforces.com/contest/617/problem/A

n = int(input())

if n % 5 == 0:
    print(n//5)
else:
    print(n//5 + 1)