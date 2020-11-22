# https://codeforces.com/problemset/problem/1373/B

for _ in range(int(input())):
    zeros = ones = 0
    for i in input():
        if i == '0':
            zeros += 1
        else:
            ones += 1

    if min(zeros, ones) % 2 == 0:
        print("NET")
    else:
        print("DA")


