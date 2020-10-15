# https://codeforces.com/problemset/problem/1173/A

x, y, z = map(int, input().split())

if x + z > y and x - z > y:
    print("+")
elif x + z < y and x - z < y:
    print("-")
elif x == y and z == 0:
    print(0)
else:
    print("?")
