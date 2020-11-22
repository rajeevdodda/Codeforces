# https://codeforces.com/problemset/problem/888/A

n = int(input())

a = tuple(map(int, input().split()))
ans = 0
for i in range(1, n-1):
    if a[i] < a[i+1] and a[i] < a[i-1] or a[i] > a[i+1] and a[i] > a[i-1]:
        ans += 1

print(ans)