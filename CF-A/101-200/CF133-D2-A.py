# https://codeforces.com/contest/133/problem/A


def single_integer():
    return int(input())


def multi_integer():
    return map(int, input().split())


def string():
    return input()


def multi_string():
    return input().split()


program = set('HQ9')

s = string()
for i in s:
    if i in program:
        print("YES")
        break
else:
    print("NO")