# https://codeforces.com/problemset/problem/1085/A

string = input()
n = len(string)
if n % 2 == 0:
    i, j = n // 2 - 1, n // 2
    while i > -1 and j < n:
        print(string[i] + string[j], end="")
        i -= 1
        j += 1
else:
    if n == 1:
        print(string)
    else:
        i, j = n // 2, n // 2 + 1
        while i > -1 and j < n:
            print(string[i] + string[j], end="")
            i -= 1
            j += 1
        print(string[0])
