# https://codeforces.com/problemset/problem/1041/A

n = int(input())

keyboards = map(int, input().split())

a, b = float('inf'), float('-inf')

for i in keyboards:
    if a > i:
        a = i
    if b < i:
        b = i

print(b - a + 1 - n)