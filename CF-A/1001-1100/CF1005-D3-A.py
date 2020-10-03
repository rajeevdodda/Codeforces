# https://codeforces.com/problemset/problem/1005/A

_ = input()

stairs = 0
steps = list()
count = 0
for i in input().split():
    if i == "1":
        stairs += 1
        if count != 0:
            steps.append(count)
        count = 1
    else:
        count += 1

steps.append(count)

print(stairs)
print(*steps)