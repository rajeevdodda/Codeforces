# https://codeforces.com/contest/483/problem/A

n, m = map(int, input().split())

# if n == 1 and m == 3:
#     print(-1)

if abs(n - m) == 1 or abs(n - m) == 0:
    print(-1)
else:
    if n % 2 != 0:
        n += 1
        if n+2 > m:
            print(-1)
        else:
            print(n, n + 1, n + 2)
    else:
        print(n, n + 1, n + 2)
