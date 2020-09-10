# https://codeforces.com/contest/160/problem/A

n = int(input())
coins = list(map(int, input().split()))
coins.sort(reverse=True)
total = sum(coins)
count = 0
temp_sum = 0
for i in coins:
    count += 1
    temp_sum += i
    total -= i
    if total < temp_sum:
        break


print(count)
