# https://codeforces.com/problemset/problem/1303/A


for _ in range(int(input())):
    string = input()

    ans = 0
    index = None
    for i in range(len(string)):
        if string[i] == '1':
            index = i
            break

    if index is not None:
        temp = 0
        for i in range(index+1, len(string)):
            if string[i] == '0':
                temp += 1
            else:
                ans += temp
                temp = 0

    print(ans)
