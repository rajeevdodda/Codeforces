# https://codeforces.com/problemset/problem/1006/A

_ = input()

for i in map(int, input().split()):
    if i % 2 == 1:
        print(i, end=" ")
    else:
        print(i - 1, end=" ")

