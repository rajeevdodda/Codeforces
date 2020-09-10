# https://codeforces.com/contest/711/problem/A

n = int(input())
rows = list()

seated = False

for i in range(n):
    row = input()
    if not seated:
        if 'OO' == row[:2]:
            rows.append("++" + row[2:])
            seated = True
        elif "OO" == row[3:]:
            rows.append(row[:3] + "++")
            seated = True
        else:
            rows.append(row)

    else:
        rows.append(row)

if seated:
    print("YES")
    for i in rows:
        print(i)
else:
    print("NO")
