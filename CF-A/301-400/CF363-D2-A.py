# https://codeforces.com/contest/363/problem/A


def single_integer():
    return int(input())


def multi_integer():
    return map(int, input().split())


def string():
    return input()


def multi_string():
    return input().split()


number = {
    "0": "O-|-OOOO",
    "1": "O-|O-OOO",
    "2": "O-|OO-OO",
    "3": "O-|OOO-O",
    "4": "O-|OOOO-",
    "5": "-O|-OOOO",
    "6": "-O|O-OOO",
    "7": "-O|OO-OO",
    "8": "-O|OOO-O",
    "9": "-O|OOOO-",

}
n = string()
for i in n[::-1]:
    print(number[i])
