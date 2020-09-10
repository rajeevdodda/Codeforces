# https://codeforces.com/contest/278/problem/A
def single_integer():
    return int(input())


def multi_integer():
    return map(int, input().split())


def string():
    return input()


def multi_string():
    return input().split()


n = single_integer()
distances = tuple(multi_integer())
a, b = multi_integer()
a -= 1
b -= 2
print("b", b)
if a == b:
    print(0)
else:
    front = 0
    i = a
    while i <= b:
        #print(i, distances[i])
        front += distances[i]
        i += 1

    back = 0
    i = n - 1 - a
    while i >= b:
        back += distances[n - 1 - i]
        i += 1
        print(i, distances[i])

    print(front)
