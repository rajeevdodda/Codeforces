# https://codeforces.com/problemset/problem/1144/A


for _ in range(int(input())):
    s = set()

    min_value = float('inf')
    max_value = float('-inf')

    for i in input():
        if ord(i) in s:
            print("NO")
            break
        else:
            s.add(ord(i))
            if ord(i) > max_value:
                max_value = ord(i)
            if ord(i) < min_value:
                min_value = ord(i)
    else:

        if len(s) == max_value - min_value + 1:
            print("YES")
        else:
            print("NO")
