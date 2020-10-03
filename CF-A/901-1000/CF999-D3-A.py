# https://codeforces.com/problemset/problem/999/A

n, k = map(int, input().split())

problems = tuple(map(int, input().split()))

i = 0
ans = 0
while i < n:
    if problems[i] <= k:
        ans += 1
    else:
        break
    i += 1
j = n - 1

while j > i:
    if problems[j] <= k:
        ans += 1
    else:
        break
    j -= 1

print(ans)
