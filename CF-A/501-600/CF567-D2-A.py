# https://codeforces.com/contest/567/problem/A
n = int(input())

coordinates = list(map(int, input().split()))

for i in range(n):
    if i == 0:
        print(abs(coordinates[i] - coordinates[i + 1]), abs(coordinates[i] - coordinates[-1]))
    elif i == n - 1:
        print(abs(coordinates[i] - coordinates[i - 1]), abs(coordinates[i] - coordinates[0]))
    else:
        print(min(abs(coordinates[i] - coordinates[i - 1]), abs(coordinates[i] - coordinates[i + 1]))
              , max(abs(coordinates[i] - coordinates[-1]), abs(coordinates[i] - coordinates[0])))
