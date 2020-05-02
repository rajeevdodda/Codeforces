# https://codeforces.com/contest/579/problem/A

n = int(input())
ans = 1
i = 0
while n // (2 ** i) != 0:
    i += 1

    if n // (2 ** i) == 1:
        if n % (2 ** i) ==0:
            break
        ans += 1
        n = n % (2 ** i)
        i = 0

print(ans)
