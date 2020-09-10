# https://codeforces.com/contest/79/problem/B


def single_integer():
    return int(input())


def multi_integer():
    return map(int, input().split())


def string():
    return input()


def multi_string():
    return input().split()


n, m, k, t = multi_integer()
wastes = list()
fruits = ["Carrots", "Kiwis", "Grapes"]

for i in range(k):
    wastes.append(tuple(multi_integer()))

for i in range(t):
    w = 0
    a, b = multi_integer()
    for j in wastes:
        if (a, b) == j:
            print("Waste")
            break
        else:
            if j[0] < a:
                w += 1
            elif j[0] == a:
                if j[1] < b:
                    w += 1
    else:
        temp = (a - 1) * m + b - 1 - w
        print(fruits[temp % 3])
