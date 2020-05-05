# https://codeforces.com/contest/275/problem/A


def single_integer():
    return int(input())


def multi_integer():
    return map(int, input().split())


def string():
    return input()


def multi_string():
    return input().split()


lights_list = list()
new_light = list()
for i in range(3):
    lights_list.append(tuple(multi_integer()))

for i in range(3):
    temp = list()
    for j in range(3):
        ans = 0
        if i == 0:
            if j == 0:
                ans = lights_list[i][j] + lights_list[i + 1][j] + lights_list[i][j + 1]
            elif j == 2:
                ans = lights_list[i][j] + lights_list[i + 1][j] + lights_list[i][j - 1]
            else:
                ans = lights_list[i][j] + lights_list[i][j + 1] + lights_list[i][j - 1] + lights_list[i + 1][j]

        elif i == 2:
            if j == 0:
                ans = lights_list[i][j] + lights_list[i - 1][j] + lights_list[i][j + 1]
            elif j == 2:
                ans = lights_list[i][j] + lights_list[i - 1][j] + lights_list[i][j - 1]
            else:
                ans = lights_list[i][j] + lights_list[i][j + 1] + lights_list[i][j - 1] + lights_list[i - 1][j]

        else:
            if j == 0:
                ans = lights_list[i][j] + lights_list[i - 1][j] + lights_list[i][j + 1] + lights_list[i + 1][j]
            elif j == 2:
                ans = lights_list[i][j] + lights_list[i - 1][j] + lights_list[i][j - 1] + lights_list[i + 1][j]
            else:
                ans = lights_list[i][j] + lights_list[i][j + 1] + lights_list[i][j - 1] + lights_list[i - 1][j] + \
                      lights_list[i + 1][j]

        if ans % 2 == 0:
            temp.append(1)
        else:
            temp.append(0)

    new_light.append(temp)

for i in new_light:
    print("".join(str(k) for k in i))
