# https://codeforces.com/problemset/problem/898/A

n = int(input())

if n % 10 == 0:
    print(n)
else:
    if n % 10 <= 5:
        print(n - n % 10)
    else:
        print(n + 10 - n % 10)
