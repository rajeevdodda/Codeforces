# https://codeforces.com/contest/334/problem/A


def single_integer():
    return int(input())


def multi_integer():
    return map(int, input().split())


def string():
    return input()


def multi_string():
    return input().split()


n = single_integer()
t = n ** 2
ans = list()
for i in range(t):
    ans.append((i + 1, t - i))


i = 0
while i < t // 2:
    for k in range(i, i + n // 2):
        print(*ans[k], end=" ")
    i += n //2
    print()
