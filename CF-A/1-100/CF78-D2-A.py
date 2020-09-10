# https://codeforces.com/contest/78/problem/A


def single_integer():
    return int(input())


def multi_integer():
    return map(int, input().split())


def string():
    return input()


def multi_string():
    return input().split()


vowels = {"a", "e", "i", "o", "u"}
answers = (5, 7, 5)
for j in answers:
    temp = 0
    s = input()
    for i in s:
        if i in vowels:
            temp += 1

    if temp != j :
        print("NO")
        break

else:
    print("YES")
