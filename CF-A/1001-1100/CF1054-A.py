# https://codeforces.com/problemset/problem/1054/A

x, y, z, t1, t2, t3 = map(int, input().split())

stairs = abs(x - y) * t1
elevator = (abs(z-x) + abs(y-x)) * t2 + t3 *3

if elevator <= stairs:
    print("YES")
else:
    print("NO")
