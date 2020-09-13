# https://codeforces.com/problemset/problem/1399/A

t = int(input())

for i in range(t):
    n = int(input())
    values = sorted(map(int, input().split()))
    for i in range(1, n):
        if values[i] - values[i-1] > 1:
            print("NO")
            break
    else:
        print("YES")