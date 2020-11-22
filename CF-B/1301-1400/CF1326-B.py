# https://codeforces.com/problemset/problem/1326/B

n = int(input())

b = tuple(map(int, input().split()))

print(b[0], end=" ")
previous = b[0]

for i in range(n - 1):
    print(previous + b[i + 1], end=" ")
    previous = max(previous, previous + b[i + 1])
