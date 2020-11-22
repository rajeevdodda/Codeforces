# https://codeforces.com/problemset/problem/910/A

n, d = map(int, input().split())

s = input()
first = 0
pointer = d
count = 0

while pointer < n:
    while pointer > first:
        if s[pointer] == '1':
            count += 1

            break
        pointer -= 1
    if pointer == first:
        print(-1)
        break
    else:
        first = pointer
        pointer += d
else:
    if first != n - 1:
        print(count+1)
    else:
        print(count)

