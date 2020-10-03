# https://codeforces.com/problemset/problem/1017/A

n = int(input())
a_sum = sum(map(int, input().split()))
rank = 1
for _ in range(n - 1):
    if a_sum < sum(map(int, input().split())):
        rank += 1

print(rank)
