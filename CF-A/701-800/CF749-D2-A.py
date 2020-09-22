# https://codeforces.com/problemset/problem/749/A

n = int(input())

a = n // 2

if n % 2 == 0:
    print(a)
    for i in range(a):
        print(2, end=" ")
else:
    print(a)
    for i in range(a-1):
        print(2, end=" ")
    print(3)