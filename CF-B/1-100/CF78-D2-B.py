# https://codeforces.com/contest/78/problem/B


def single_integer():
    return int(input())


def multi_integer():
    return map(int, input().split())


def string():
    return input()


def multi_string():
    return input().split()


n = single_integer()

colors = "ROYGBIV"
c_list = ["", "G", "GB", "YGB", "YGBI", "OYGBI", "OYGBIV"]
print(colors * (n // 7) + c_list[n % 7])
