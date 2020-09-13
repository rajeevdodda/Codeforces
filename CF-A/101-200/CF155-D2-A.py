# https://codeforces.com/problemset/problem/155/A


n = int(input())

scores = tuple(map(int, input().split()))

ans = 0

min_value, max_value = scores[0], scores[0]
if n == 1:
    print(0)
else:
    for i in range(1, n):
        if scores[i] > max_value:
            max_value = scores[i]
            ans += 1
        elif scores[i] < min_value:
            min_value = scores[i]
            ans += 1
    print(ans)