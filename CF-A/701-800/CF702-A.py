# https://codeforces.com/problemset/problem/702/A

n = int(input())

array = tuple(map(int, input().split()))

final_ans = ans = 1

if n != 1:
    for i in range(1, n):
        if array[i - 1] < array[i]:
            ans += 1
        else:
            final_ans = max(final_ans, ans)
            ans = 1


print(max(final_ans, ans))