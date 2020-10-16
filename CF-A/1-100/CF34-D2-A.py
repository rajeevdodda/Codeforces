# https://codeforces.com/problemset/problem/34/A

n = int(input())

a = tuple(map(int, input().split()))
index1, index2 = None, None
min_value = float('inf')

for i in range(1, n):
    if min_value > abs(a[i] - a[i - 1]):
        min_value = abs(a[i] - a[i - 1])
        index1, index2 = i, i + 1

if min_value > abs(a[0] - a[n - 1]):
    print(1, n)
else:
    print(index1, index2)
