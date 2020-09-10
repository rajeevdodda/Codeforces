# https://codeforces.com/contest/584/problem/A

n, t = map(int, input().split())

base = 10 ** (n - 1)
i = base

while i < base + 9:
    if i % t == 0:
        print(i)
        break
    else:
        i += 1
else:
    print(-1)



