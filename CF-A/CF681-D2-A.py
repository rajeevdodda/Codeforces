# https://codeforces.com/contest/681/problem/A
n = int(input())

for i in range(n):
    name, a, b = input().split()
    if int(b) > int(a) >= 2400:
        print("YES")
        break
else:
    print("NO")
