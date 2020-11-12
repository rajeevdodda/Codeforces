# https://codeforces.com/problemset/problem/1433/B

for _ in range(int(input())):
    n = int(input())
    s = tuple(input().split())
    i = 0
    first = None
    second = None
    while i < n:
        if s[i] == '1':
            first = i
            break
        i += 1
    i = n - 1
    while i > - 1:
        if s[i] == '1':
            second = i
            break
        i -= 1

    if first == second:
        print(0)
    else:
        ans = 0
        for i in range(first, second):
            if s[i] == '0':
                ans += 1
        print(ans)

