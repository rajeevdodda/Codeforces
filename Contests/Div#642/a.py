def single_integer():
    return int(input())


def multi_integer():
    return map(int, input().split())


def string():
    return input()


def multi_string():
    return input().split()


n = single_integer()

for i in range(n):
    n, m = multi_integer()

    if n == 1:
        print(0)
    elif n == 2:
        print(m)
    else:
        print(2 * m)
