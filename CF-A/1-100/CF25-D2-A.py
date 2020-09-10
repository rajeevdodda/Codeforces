# https://codeforces.com/contest/25/problem/A


def single_integer():
    return int(input())


def multi_integer():
    return map(int, input().split())


def string():
    return input()


def multi_string():
    return input().split()


n = single_integer()
numbers = tuple(multi_integer())

for i in range(1, n - 1):
    t = numbers[i - 1] % 2
    if numbers[i] % 2 == t:
        if numbers[i+1] % 2 == t:
            pass
        else:
            print(i+2)
            break
    else:
        if numbers[i+1]%2 == t:
            print(i+1)
            break
        else:
            print(i)
            break





