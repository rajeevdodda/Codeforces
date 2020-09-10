# http://codeforces.com/contest/102/problem/B


def single_integer():
    return int(input())


def multi_integer():
    return map(int, input().split())


def string():
    return input()


def multi_string():
    return input().split()


n = string()
ans = 0

while True:
    if int(n) <= 9:
        break
    else:
        ans += 1
        temp = 0
        for i in n:
            temp += int(i)
        n = str(temp)
print(ans)
