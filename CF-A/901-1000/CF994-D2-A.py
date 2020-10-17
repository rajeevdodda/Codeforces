# https://codeforces.com/problemset/problem/994/A

n, m = input().split()

sequence = input().split()

finger = tuple(input().split())

for i in sequence:
    if i in finger:
        print(i, end=" ")