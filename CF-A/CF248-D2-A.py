#


def single_integer():
    return int(input())


def multi_integer():
    return map(int, input().split())


def string():
    return input()


def multi_string():
    return input().split()


n = single_integer()
l_open = 0
l_close = 0
r_open = 0
r_close = 0

for i in range(n):
    l, r = multi_string()
    if l == "1":
        l_open += 1
    else:
        l_close += 1

    if r == "1":
        r_open += 1
    else:
        r_close += 1

print(min(l_open, l_close) + min(r_open, r_close))
