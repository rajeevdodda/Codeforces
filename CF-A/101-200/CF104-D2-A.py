# https://codeforces.com/problemset/problem/104/A

n = int(input())

ans = n - 10

if ans == 10:
    print(15)
elif ans == 11:
    print(4)
elif ans < 1 or ans > 10:
    print(0)
else:
    print(4)
