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

    if k % (n - 1) == 0:
        ans = ((k // (n - 1)) * n) - 1
        print(ans)
    else:
        ans = (k // (n - 1)) * n + (k % (n -1))
        print(ans)
