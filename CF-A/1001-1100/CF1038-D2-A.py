# https://codeforces.com/problemset/problem/1038/A

n, k = map(int, input().split())

alpha_dict = dict()

for i in input():
    alpha_dict[i] = alpha_dict.get(i, 0) + 1

if chr(64 + k) not in alpha_dict or len(alpha_dict) != k:
    print(0)
else:
    min_value = min(alpha_dict.values())
    print(min_value * k)
