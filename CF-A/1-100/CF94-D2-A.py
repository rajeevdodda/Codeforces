# https://codeforces.com/contest/94/problem/A


def single_integer():
    return int(input())


def multi_integer():
    return map(int, input().split())


def string():
    return input()


def multi_string():
    return input().split()


n = input()
numbers_dict = dict()
for i in range(10):
    numbers_dict[input()] = i
i = 0
while i < 80:
    s = numbers_dict[n[i:i + 10]]
    print(s, end="")
    i += 10
