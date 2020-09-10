# https://codeforces.com/contest/546/problem/A

k, n, w = map(int, input().split())

temp = w * k * (w + 1) // 2 - n

if temp < 0:
    print(0)
else:
    print(temp)