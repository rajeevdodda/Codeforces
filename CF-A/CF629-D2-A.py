# http://codeforces.com/contest/629/problem/A
n = int(input())

columns = dict()
total = 0
for i in range(n):
    row = input()
    row_count = 0
    for j in range(n):
        if row[j] == 'C':
            row_count += 1
            columns[j] = columns.get(j, 0) + 1
    if row_count >= 2:
        total += (row_count * (row_count - 1)//2)


for v in columns.values():
    total += (v * (v - 1) // 2)

print(total)

