def single_integer():
    return int(input())


def multi_integer():
    return map(int, input().split())


def string():
    return input()


def multi_string():
    return input().split()


n = single_integer()

for i in range(n):
    number = single_integer()
    count = 0
    d = 10
    sample = list()

    while True:
        sample.append(number % d)
        if number % d != 0:
            count +=1
        number = number // d
        if number == 0:
            break
    print(count)
    k = 0
    for j in sample:
        if j != 0:
            print((10**k) *j, end=" ")
        k += 1

    print()
