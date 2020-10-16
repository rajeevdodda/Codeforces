# https://codeforces.com/problemset/problem/1106/A

n = int(input())

if n < 3:
    print(0)
else:
    matrix = list()

    for i in range(n):
        matrix.append(input())
    ans = 0
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            if matrix[i][j] == 'X' and matrix[i - 1][j - 1] == 'X' and matrix[i - 1][j + 1] == 'X' and matrix[i + 1][
                j - 1] == 'X' and \
                    matrix[i + 1][j + 1] == 'X':
                ans += 1
    print(ans)
