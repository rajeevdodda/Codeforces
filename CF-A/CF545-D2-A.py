# https://codeforces.com/contest/545/problem/A


def single_integer():
    return int(input())


def multi_integer():
    return map(int, input().split())


def string():
    return input()


def multi_string():
    return input().split()


n = single_integer()

ans = 0
cars = list()
for i in range(n):
    for j in multi_string():
        if j == '1' or j == "3":
            break
    else:
        ans += 1
        cars.append(i+1)

print(ans)
print(*cars)
