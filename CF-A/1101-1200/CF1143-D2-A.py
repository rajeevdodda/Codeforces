# https://codeforces.com/problemset/problem/1143/A

n = int(input())

i = 1
left = right = None

for k in input().split():
    if k == '0':
        left = i
    else:
        right = i
    i += 1

print(min(left, right))
