# https://codeforces.com/contest/330/problem/A


def single_integer():
    return int(input())


def multi_integer():
    return map(int, input().split())


def string():
    return input()


def multi_string():
    return input().split()


r, c = multi_integer()
columns = set()
good_row = 0
ans = 0
for i in range(r):
    k = 0
    count = 0
    row = string()
    for j in row:
        if j == 'S':
            count += 1
            columns.add(k)
        k += 1
    if count == 0:
        good_row += 1
        ans += c

print(ans + (c-len(columns)) * (r - good_row ))
