# https://codeforces.com/contest/16/problem/B


def single_integer():
    return int(input())


def multi_integer():
    return map(int, input().split())


def string():
    return input()


def multi_string():
    return input().split()


n, m = multi_integer()

matches = list()
for i in range(m):
    matches.append(tuple(multi_integer()))

matches.sort(key=lambda x: x[1], reverse=True)
ans = 0

for i in matches:
    if n > i[0]:
        n -= i[0]
        ans += (i[1] * i[0])
    else:
        ans += (i[1] * n)
        n = 0
    if n == 0:
        break

print(ans)
