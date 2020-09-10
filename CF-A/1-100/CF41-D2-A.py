# https://codeforces.com/contest/41/problem/A
a = input()
b = input()
if a == b[::-1]:
    print("YES")
else:
    print("NO")