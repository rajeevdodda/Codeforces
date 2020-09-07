# https://codeforces.com/contest/129/problem/B


def single_integer():
    return int(input())


def multi_integer():
    return map(int, input().split())


def string():
    return input()


def multi_string():
    return input().split()


n, m = multi_integer()
ans_dict = dict()
for i in range(m):
    a, b = multi_integer()
    ans_dict[a] = ans_dict.get(a, 0) + 1
    ans_dict[b] = ans_dict.get(b, 0) + 1

ans = 0
for key, value in ans_dict.items():
    if value > 1:
        ans += 1

print(ans)
