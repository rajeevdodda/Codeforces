# https://codeforces.com/contest/1204/problem/A

binary_string = input()
j = 0
ans = 0
for i in binary_string[::-1]:
    ans += int(i) * (2) ** j
    j += 1

total = 0
i = 0
while 4 ** i < ans:
    i += 1
    total += 1

print(total)
