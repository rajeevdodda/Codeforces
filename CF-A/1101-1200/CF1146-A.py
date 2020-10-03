# https://codeforces.com/problemset/problem/1146/A
a_count = 0

length = 0

for i in input():
    if i == "a":
        a_count += 1
    length += 1

if 2 * a_count > length:
    print(length)
else:
    print(2 * a_count - 1)
