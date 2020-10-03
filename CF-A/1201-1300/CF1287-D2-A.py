# https://codeforces.com/problemset/problem/1287/A

for _ in range(int(input())):
    n = int(input())
    string = input()
    index = None
    count = 0
    for i in range(n):
        if string[i] == "A":
            index = i
            break
    if index is None or index == n - 1:
        print(0)
    else:
        temp = 0
        for i in range(index, n):
            if string[i] == "P":
                temp += 1
            else:
                count = max(temp, count)
                temp = 0

        count = max(temp, count)
        print(count)