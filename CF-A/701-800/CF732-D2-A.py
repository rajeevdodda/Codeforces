# https://codeforces.com/contest/732/problem/A
k, r = map(int, input().split())
for i in range(1, 10):
    temp = k * i
    if temp % 10 == 0 or temp % 10 == r:
        print(i)
        break
