# https://codeforces.com/problemset/problem/712/A

n = int(input())

t = tuple(map(int, input().split()))

for i in range(1, n):
    print(t[i - 1] + t[i], end=" ")
print(t[-1])
