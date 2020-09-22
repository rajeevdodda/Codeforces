# https://codeforces.com/problemset/problem/1367/B

t = int(input())

for i in range(t):
    n = int(input())
    array = tuple(map(int, input().split()))
    even = odd = 0
    for k in range(n):
        if k % 2 != array[k] % 2:
            if k % 2 == 0:
                even += 1
            else:
                odd += 1

    if odd == even:
        print(odd)

    else:
        print(-1)

