# https://codeforces.com/contest/401/problem/A

def single_integer():
    return int(input())


def multi_integer():
    return map(int, input().split())


def string():
    return input()


def multi_string():
    return input().split()


n, x = multi_integer()

total_sum = sum(multi_integer())

if total_sum == 0:
    print(0)
elif total_sum > 0:
    ans = 0
    while total_sum > 0:
        total_sum -= x
        ans += 1
    print(ans)
else:
    ans = 0
    while total_sum < 0:
        total_sum += x
        ans += 1
    print(ans)
