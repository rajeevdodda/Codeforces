# https://codeforces.com/contest/768/problem/A
n = int(input())
stewards = tuple(map(int, input().split()))

minimum, maximum = float('inf'), float('-inf')

for i in stewards:
    if i > maximum:
        maximum = i
    if i < minimum:
        minimum = i

count = 0
for i in stewards:
    if minimum < i < maximum:
        count += 1

print(count)
