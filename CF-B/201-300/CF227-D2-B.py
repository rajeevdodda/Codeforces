# https://codeforces.com/contest/227/problem/B


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
positions = dict()
for i, j in enumerate(numbers, start=1):
    positions[j] = i

m = single_integer()
queries = multi_integer()

vasya = 0
petya = 0

for i in queries:
    temp = positions[i]
    vasya += temp
    petya += (n - temp + 1)

print(vasya, petya)
