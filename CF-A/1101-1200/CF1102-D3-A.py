# https://codeforces.com/problemset/problem/1102/A

n = int(input()) % 4

if n == 0 or n == 3:
    print(0)
elif n == 1 or n == 2:
    print(1)