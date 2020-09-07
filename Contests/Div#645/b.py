# https://codeforces.com/contest/1358/problem/B


def single_integer():
    return int(input())


def multi_integer():
    return map(int, input().split())


def string():
    return input()


def multi_string():
    return input().split()


t = single_integer()

for i in range(t):
    n = single_integer()
    a_values = sorted(multi_integer())
    print(a_values)
    a_dict = dict()
    for k in a_values:
        a_dict[k] = a_dict.get(k, 0) + 1
    print(a_dict)
    ans = 1
    j = 0
    while j < n:
        if a_values[j] <= ans:
            ans += 1
            j += 1

    # for key in a_dict.keys():
    #     if key <= ans:
    #         ans += a_dict[key]
    #     elif key < a_dict[key] + ans:
    #         ans += a_dict[key]
    #     else:
    #

    print(ans)


