# https://codeforces.com/contest/551/problem/A
n = int(input())

numbers = tuple(map(int, input().split()))
sorted_numbers = sorted(numbers, reverse=True)
rank = 1
numbers_dict = dict()
for i in sorted_numbers:
    if i in numbers_dict:
        pass
    else:
        numbers_dict[i] = rank
    rank += 1

for i in numbers:
    print(numbers_dict[i], end=" ")