# https://codeforces.com/contest/447/problem/A


def single_integer():
    return int(input())


def multi_integer():
    return map(int, input().split())


def string():
    return input()


def multi_string():
    return input().split()


p, n = multi_integer()
table = set()

for i in range(n):
    t = int(input())
    if t % p not in table:
        table.add(t % p)
    else:
        print(i+1)
        break
else:
    print(-1)


