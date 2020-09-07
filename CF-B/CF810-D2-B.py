# https://codeforces.com/contest/810/problem/B


def single_integer():
    return int(input())


def multi_integer():
    return map(int, input().split())


def string():
    return input()


def multi_string():
    return input().split()


n, f = multi_integer()
ans = 0
f_list = list()

for i in range(n):
    k, l = multi_integer()
    if l <= k:
        ans += l
    else:
        ans += k
        f_list.append(min(k, l - k))

f_list.sort(reverse=True)
i = 0

if f_list:
    while i < f and i < len(f_list):
        ans += f_list[i]
        i += 1

print(ans)
