def single_integer():
    return int(input())


def multi_integer():
    return map(int, input().split())


def string():
    return input()


def multi_string():
    return input().split()


k = single_integer()
for i in range(k):
    n, m = multi_integer()
    if max(n, m) >= 3:
        if min(n, m) >= 2:
            print("NO")
        else:
            print("YES")
    else:
        print("YES")
