# https://codeforces.com/problemset/problem/1206/B

n = input()

zeros = 0
total = 0
ones = 0
for i in map(int, input().split()):
    if i == 0:
        zeros += 1

    else:
        if i < 0:
            total += abs(i - (-1))
            ones += 1
        else:
            total += abs(i - 1)

if ones % 2 == 0:
    print(total + zeros)
else:
    if zeros != 0:
        print(total + zeros)
    else:
        print(total + 2)
