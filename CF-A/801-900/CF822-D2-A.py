# https://codeforces.com/problemset/problem/822/A

min_value = min(map(int, input().split()))

ans = 1

for i in range(min_value, 1, -1):
    ans *= i

print(ans)