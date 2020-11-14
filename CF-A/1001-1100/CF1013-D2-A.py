# https://codeforces.com/problemset/problem/1013/A

n = input()

x = sum(map(int, input().split()))
y = sum(map(int, input().split()))

if y <= x:
    print("Yes")
else:
    print("No")
