# https://codeforces.com/problemset/problem/1230/A


a, b, c, d = sorted(map(int, input().split()))

if a + b + c == d:
    print("YES")
elif a + c == b + d:
    print("YES")
elif a + d == b + c:
    print("YES")
else:
    print("NO")