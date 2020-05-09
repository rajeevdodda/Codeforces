# https://codeforces.com/contest/424/problem/A


def single_integer():
    return int(input())


def multi_integer():
    return map(int, input().split())


def string():
    return input()


def multi_string():
    return input().split()


n = single_integer()
x_string = string()
x_count = 0
X_count = 0
final_string = ""

for i in x_string:
    if i == "x":
        x_count += 1
    else:
        X_count += 1

if x_count == X_count:
    print(0)
    print(x_string)
else:

    diff = abs(n // 2 - max(x_count, X_count))
    print(diff)
    if x_count > X_count:
        for i in x_string:
            if diff > 0:
                if i == "x":
                    final_string += "X"
                    diff -= 1
                else:
                    final_string += i
            else:
                final_string += i
    else:

        for i in x_string:
            if diff > 0:
                if i == "X":
                    final_string += "x"
                    diff -= 1
                else:
                    final_string += i
            else:
                final_string += i
    print(final_string)

