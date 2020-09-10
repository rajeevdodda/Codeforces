# https://codeforces.com/problemset/problem/116/A

n = int(input())
max_value = 0
ans = 0
for i in range(n):
    a, b = input().split()
    ans -= int(a)
    ans += int(b)
    if ans > max_value:
        max_value = ans

print(max_value)
