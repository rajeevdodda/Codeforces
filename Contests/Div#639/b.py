def single_integer():
    return int(input())


def multi_integer():
    return map(int, input().split())


def string():
    return input()


def multi_string():
    return input().split()


t = single_integer()
ans = 0

h = 1
for i in range(t):
    n = single_integer()
    while True:
        cards = h * ((3 * h + 1) / 2)
        #print(cards)
        if n == 1:
            break
        if cards < n:
            temp = cards
            h += 1
        elif cards == n:
            ans += 1
            break
        else:
            n = n - temp
            h = 1
            ans += 1
    print(ans)
    h = 1
    ans = 0


