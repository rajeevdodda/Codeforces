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

for i in range(n):
    temp = (single_integer() -1) // 2
    print(str(int(4 * (temp + 1) * temp * (2 * temp + 1) / 3)))
