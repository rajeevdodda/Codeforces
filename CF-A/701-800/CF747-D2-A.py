# https://codeforces.com/problemset/problem/747/A
import math
n = int(input())

a = int(math.sqrt(n))

if a * a == n:
    print(a, a)
else:
    for i in range(a+1, 0, -1):
        if n % i == 0:
            print(min(i, n//i), max(i, n//i))
            break
