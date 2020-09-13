# https://codeforces.com/problemset/problem/750/A

n, k = map(int, input().split())

total = 0
for i in range(1, n+1):
    total += i * 5
    if k - (240 - total) > 0:
        print(i - 1)
        break
else:
    print(n)