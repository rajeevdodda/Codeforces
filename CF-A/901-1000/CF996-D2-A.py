# https://codeforces.com/problemset/problem/996/A

n = int(input())

ans = 0


for i in (100, 20, 10, 5, 1):
    ans += n // i
    n = n % i

    if n ==  0:
        break

print(ans)