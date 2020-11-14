# https://codeforces.com/problemset/problem/1178/A

n = int(input())

parties = tuple(map(int, input().split()))

total = parties[0]
ans = parties[0]

s = [1]

for i in range(1, n):
    if parties[i] * 2 <= parties[0]:
        ans += parties[i]
        s.append(i + 1)
    total += parties[i]


if 2 * ans > total:
    print(len(s))
    print(*s)
else:
    print(0)
