# https://codeforces.com/problemset/problem/1191/A

a = int(input()) % 4

if a == 1:
    print(0, "A")
elif a == 2:
    print(1, "B")
elif a == 3:
    print(2, "A")
else:
    print(1, "A")