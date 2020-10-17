# https://codeforces.com/problemset/problem/992/A

n = input()
elements = set(map(int, input().split()))

if 0 in elements:
    print(len(elements) -1)
else:
    print(len(elements))