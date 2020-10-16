# https://codeforces.com/problemset/problem/1152/A

n, m = input().split()

chest_odd, chest_even, keys_odd, key_even = 0, 0, 0, 0

for i in map(int, input().split()):
    if i % 2 == 0:
        chest_even += 1
    else:
        chest_odd += 1

for i in map(int, input().split()):
    if i % 2 == 0:
        key_even += 1
    else:
        keys_odd += 1

print(min(chest_even, keys_odd) + min(chest_odd, key_even))
