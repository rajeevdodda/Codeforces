# https://codeforces.com/contest/404/problem/A

n = int(input())
stack = list()
row_set = set()

for i in range(n):

    row = input()
    if not row_set:
        row_set.update(row)
        if len(row_set) != 2:
            print("NO")
            break

    if set(row) != row_set:
        print("NO")
        break

    if i < n // 2:
        stack.append(row)
    elif i == n // 2:
        if row[:n // 2 + 1] != row[n // 2:][::-1]:
            print("NO")
            break

    else:
        if stack.pop() != row:
            print("NO")
            break
else:
    print("YES")
