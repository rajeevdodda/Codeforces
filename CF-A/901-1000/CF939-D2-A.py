# https://codeforces.com/problemset/problem/939/A

n = int(input())

planes = tuple(map(int, input().split()))

for i in range(n):
    if planes[planes[planes[i] - 1] - 1] == i + 1:
        print("YES")
        break
else:
    print("NO")
