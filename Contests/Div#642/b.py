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

    a = list(multi_integer())
    a.sort()

    b = list(multi_integer())
    b.sort(reverse=True)
    j = 0
    while j < k:
        if b[j] <= a[j]:
            break
        else:
            a[j], b[j] = b[j], a[j]
            j += 1

    print(sum(a))
