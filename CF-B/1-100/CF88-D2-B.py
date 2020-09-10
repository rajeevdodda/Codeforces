# https://codeforces.com/contest/88/problem/B


def single_integer():
    return int(input())


def multi_integer():
    return map(int, input().split())


def string():
    return input()


def multi_string():
    return input().split()


import math

n, m, x = multi_integer()
alpha_dict = dict()
shift_list = list()
near_to_shift = set()
total_letters = set()

for i in range(n):
    for j, key in enumerate(string(), start=0):
        if key == "S":
            shift_list.append((i, j))
        else:
            total_letters.add(key)
            alpha_dict[(i, j)] = key
q = single_integer()
s = string()

for k, v in alpha_dict.items():
    if v not in near_to_shift:
        for i in shift_list:
            if math.sqrt((i[0] - k[0]) ** 2 + (i[1] - k[1]) ** 2) <= x:
                near_to_shift.add(v)
                break
ans = 0

for i in s:
    if i.lower() not in total_letters:
        print(-1)
        break

    if not shift_list and i.isupper():
        print(-1)
        break
    if i.isupper():
        if i.lower() not in near_to_shift:
            ans += 1

else:
    print(ans)
