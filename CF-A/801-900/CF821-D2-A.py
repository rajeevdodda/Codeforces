# https://codeforces.com/problemset/problem/821/A
import sys

n = int(input())
l = list()

for i in range(n):
    l.append(tuple(map(int, input().split())))

for i in range(n):
    for j in range(n):

        if l[i][j] == 1:
            continue
        else:
            if i == 0 and j == 0:
                if l[i][j] != l[i + 1][j] + l[j + 1][i]:
                    print("NO")
                    sys.exit(-1)
            elif i == 0 and j == n - 1:
                if l[i][j] != l[i + 1][j] + l[j - 1][i]:
                    print("NO")
                    sys.exit(-1)
            elif i == n - 1 and j == 0:
                if l[i][j] != l[i - 1][j] + l[j + 1][i]:
                    print("NO")
                    sys.exit(-1)
            elif i == n - 1 and j == n - 1:
                if l[i][j] != l[i - 1][j] + l[j - 1][i]:
                    print("NO")
                    sys.exit(-1)

            elif i == 0 and j != 0:
                if l[i][j] != l[i + 1][j] + l[j + 1][i] or l[i][j] != l[i + 1][j] + l[j - 11][i]:
                    print("NO")
                    sys.exit(-1)
            elif i == n - 1 and j != 0:
                if l[i][j] != l[i - 1][j] + l[j + 1][i] or l[i][j] != l[i - 1][j] + l[j - 11][i]:
                    print("NO")
                    sys.exit(-1)
            elif i == 0 and j != 0:
                if l[i][j] != l[i + 1][j] + l[j + 1][i] or l[i][j] != l[i + 1][j] + l[j - 1][i]:
                    print("NO")
                    sys.exit(-1)
            elif i != 0 and j == 0:
                if l[i][j] != l[i + 1][j] + l[j + 1][i] or l[i][j] != l[i - 1][j] + l[j - 1][i]:
                    print("NO")
                    sys.exit(-1)
