# https://codeforces.com/problemset/problem/831/B
first = input()
second = input()

string = input()

k = 0
sample = dict()
for i in first:
    sample[i] = k
    k += 1

for i in string:
    if i.isnumeric():
        print(i, end="")
    else:
        temp = i.isupper()
        index = sample[i.lower()]

        if temp:
            print(second[index].upper(), end="")
        else:
            print(second[index], end="")
