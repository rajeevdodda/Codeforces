# https://codeforces.com/problemset/problem/177/A1

n = int(input())
ans = 0
for i in range(n):
    numbers = tuple(map(int, input().split()))
    if i == n // 2:
        ans += sum(numbers)
    else:
        ans += numbers[i % (n // 2)] + numbers[n // 2] + numbers[n  - 1 - (i % (n // 2))]
print(ans)

