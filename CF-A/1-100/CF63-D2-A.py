# https://codeforces.com/contest/63/problem/A


def single_integer():
    return int(input())


def multi_integer():
    return map(int, input().split())


def string():
    return input()


def multi_string():
    return input().split()


n = single_integer()
row = dict()

status_dict = {
    "rat": 1,
    "woman": 2,
    "child": 2,
    "man": 3,
    "captain": 4
}

for i in range(n):
    name, status = multi_string()
    s = status_dict[status]
    if s in row:
        row[s].append(name)
    else:
        row[s] = [name]

for i in sorted(row.keys()):
    for j in row[i]:
        print(j)
