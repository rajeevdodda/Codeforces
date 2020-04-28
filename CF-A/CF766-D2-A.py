# https://codeforces.com/contest/766/problem/A
a = input()
b = input()
if a == b:
    print(-1)
else:
    print(max(len(a), len(b)))