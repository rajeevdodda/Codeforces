# https://codeforces.com/problemset/problem/767/A

n = int(input())
stack = list()
snack = tuple(map(int, input().split()))
for i in range(n):
    if not stack:
        stack.append(snack[i])
    else:
        if snack[i] > stack[-1]:
            stack.append(snack[i])
            print()
        else:
            print(*stack[::-1])
            stack = [snack[i]]

print(*stack[::-1])
