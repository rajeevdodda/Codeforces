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
    n, k = multi_integer()
    temp_1 = n - (k - 1)
    temp_2 = n - (k - 1) * 2
    if temp_1 > 0:
        if temp_1 % 2 == 1:
            print("YES")
            for j in range(k-1):
                print(1, end=" ")
            print(temp_1)
            continue
    if temp_2 > 0:
        if temp_2 % 2 == 0:
            print("YES")
            for j in range(k - 1):
                print(2, end=" ")
            print(temp_2)
            continue
    print("NO")



