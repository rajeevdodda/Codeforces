# https://codeforces.com/contest/742/problem/A


n = int(input())
power_dict = {
    0: 6,
    1: 8,
    2: 4,
    3: 2
}


if n == 0:
    print(1)
else:
    print(power_dict[n%4])
