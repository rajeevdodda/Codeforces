# https://codeforces.com/problemset/problem/1398/B

for _ in range(int(input())):
    string = input()
    temp = list()
    count = 0
    for i in range(len(string)):
        if string[i] == '1':
            count += 1
        else:
            if count != 0:
                temp.append(count)
            count = 0
    if count != 0:
        temp.append(count)

    print(sum(sorted(temp, reverse=True)[0::2]))