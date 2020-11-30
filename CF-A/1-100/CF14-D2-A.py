# https://codeforces.com/problemset/problem/14/A

n, m = map(int, input().split())

i_min = float('inf')
j_min = float('inf')
i_max = float('-inf')
j_max = float('-inf')
x = None
top = None
bottom = None
new = list()
for i in range(n):
    line = input()
    for k in range(m):
        if line[k] == "*":
            i_min = j_min = k
            break
    for k in range(m-1, -1, -1):
        if line[k] == "*":
            i_max = j_max = k
            top = i
            bottom = i
            break

    new.append(line)
    if top is not None:

        x = i
        break


for i in range(x+1, n):

    line = input()
    for k in range(m):
        if line[k] == "*":
            j_min = min(k, j_min)
            break
    for k in range(m-1, -1, -1):
        if line[k] == "*":
            j_max = max(k, j_max)
            bottom = i
    new.append(line)


for i in range(top, bottom+1):
    print(new[i][min(i_min, j_min): max(j_max, i_max)+1])


