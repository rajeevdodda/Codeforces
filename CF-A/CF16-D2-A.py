# https://codeforces.com/contest/16/problem/A


def single_integer():
    return int(input())


def multi_integer():
    return map(int, input().split())


def string():
    return input()


def multi_string():
    return input().split()


n, m = multi_integer()
previous_color = None
ans = True
for i in range(n):
    row = string()
    if i == 0:
        current_color = row[0]
        for j in row[1:]:
            if j != current_color:
                ans = False
                break
        else:
            previous_color = current_color
    else:
        current_color = row[0]
        for j in row[1:]:
            if j != current_color or j == previous_color:
                ans = False
                break
        else:
            previous_color = current_color
    if not ans:
        print("NO")
        break
else:
    print("YES")
