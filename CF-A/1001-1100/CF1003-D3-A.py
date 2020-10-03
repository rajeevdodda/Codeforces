# https://codeforces.com/problemset/problem/1003/A

_ = input()

hash_map = dict()

max_value = 0
for i in input().split():
    hash_map[i] = hash_map.get(i, 0) + 1

    max_value = max(hash_map[i], max_value)


print(max_value)