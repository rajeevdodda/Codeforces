# https://codeforces.com/problemset/problem/157/A

n = int(input())
rows = list()
for i in range(n):
    rows.append(tuple(map(int, input().split())))

ans = 0

for i in range(n):
    rows_total = sum(rows[i])
    for k in range(n):
        columns_total = 0

        for j in rows:
            columns_total += j[k]
        if rows_total < columns_total:
            ans += 1

print(ans)