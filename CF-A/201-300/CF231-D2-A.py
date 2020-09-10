# https://codeforces.com/contest/231/problem/A

n = int(input())
ans = 0
# for i in range(n):
#     problems = map(int, input().split())
#     if sum(problems) >= 2:
#         ans += 1

for i in range(n):
    problems = input().split()
    temp = 0
    for j in problems:
        if j == '1':
            temp += 1
            if temp == 2:
                ans += 1
                break


print(ans)
