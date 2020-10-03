# https://codeforces.com/problemset/problem/1114/A

x, y, z = map(int, input().split())
a, b, c = map(int, input().split())

if x > a:
    print("NO")
elif y > (a+b-x):
    print("NO")
elif z > a + b + c - x -y:
    print("NO")
else:
    print("YES")