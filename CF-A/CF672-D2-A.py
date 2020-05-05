# https://codeforces.com/contest/672/problem/A

n = int(input())
a = ""
for i in range(1, 1001):
    a += str(i)
    if len(a) >= n:
        print(a[n-1])
        break


