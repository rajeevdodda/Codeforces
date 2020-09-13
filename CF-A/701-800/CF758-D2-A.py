# https://codeforces.com/problemset/problem/758/A

n = int(input())

welfare = tuple(map(int, input().split()))

max_value = max(welfare)

ans = 0

for i in welfare:
    ans += (max_value - i)

print(ans)

