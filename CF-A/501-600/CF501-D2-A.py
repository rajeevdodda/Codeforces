# https://codeforces.com/contest/501/problem/A


def single_integer():
    return int(input())


def multi_integer():
    return map(int, input().split())


def string():
    return input()


def multi_string():
    return input().split()


a, b, c, d = multi_integer()

misha_points = max((3*a/10), (a - (a/250)*c))
vasya_points = max((3*b/10), (b - (b/250)*d))

if misha_points > vasya_points:
    print("Misha")
elif misha_points == vasya_points:
    print("Tie")
else:
    print("Vasya")