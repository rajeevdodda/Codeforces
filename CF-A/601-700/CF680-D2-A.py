# https://codeforces.com/problemset/problem/680/A

sample_dict = dict()

total = 0
for i in map(int, input().split()):
    sample_dict[i] = sample_dict.get(i, 0) + 1
    total += i


max_value = float('-inf')
for key, value in sample_dict.items():
    if value >= 2:
        if max_value < key * (min(value, 3)):
            max_value = key * (min(value, 3))
if max_value == float('-inf'):
    max_value = 0

print(total-max_value)
