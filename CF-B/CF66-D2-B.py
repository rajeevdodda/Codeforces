# https://codeforces.com/contest/66/problem/B


def single_integer():
    return int(input())


def multi_integer():
    return map(int, input().split())


def string():
    return input()


def multi_string():
    return input().split()


n = single_integer()

tiles = tuple(multi_integer())
max_len = 0
for i in range(n):
    temp = 0
    tile = tiles[i]

    j = i
    while j >= 0:
        if tile >= tiles[j]:
            temp += 1
            tile = tiles[j]
            j -= 1
        else:
            break

    k = i + 1
    tile = tiles[i]
    while k < n:
        if tile >= tiles[k]:
            temp += 1
            tile = tiles[k]
            k += 1
        else:
            break
    if temp > max_len:
        max_len = temp

print(max_len)
