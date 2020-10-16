# https://codeforces.com/problemset/problem/937/A


_ = input()

scores = set(input().split())

if '0' in scores:
    print(len(scores) - 1)
else:
    print(len(scores))