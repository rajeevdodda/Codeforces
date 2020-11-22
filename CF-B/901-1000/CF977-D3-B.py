# https://codeforces.com/problemset/problem/977/B

n = int(input())
s = input()

hash_map = dict()

max_value = 0
max_two_gram = None
for i in range(0, n - 1):
    two_gram = s[i:i + 2]
    hash_map[two_gram] = hash_map.get(two_gram, 0) + 1

    if hash_map[two_gram] > max_value:
        max_value = hash_map[two_gram]
        max_two_gram = two_gram

print(max_two_gram)
