#


def single_integer():
    return int(input())


def multi_integer():
    return map(int, input().split())


def string():
    return input()


def multi_string():
    return input().split()


s = string()
max_letter = s[0]
count = 1
for i in s[1:]:
    if i > max_letter:
        max_letter, count = i, 1
    elif i == max_letter:
        count += 1

print(max_letter*count)
