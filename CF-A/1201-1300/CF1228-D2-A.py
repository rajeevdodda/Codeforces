# https://codeforces.com/problemset/problem/1228/A

a, b = map(int, input().split())


def unique_number(number):
    s = set()

    while number != 0:
        if number % 10 in s:
            return True
        else:
            s.add(number % 10)
            number = number // 10
    return False


while unique_number(a):
    a += 1
    if a > b:
        print(-1)
        break

else:
    print(a)
