# https://codeforces.com/problemset/problem/1301/A

for _ in range(int(input())):
    a_string = input()
    b_string = input()
    c_string = input()

    for i in range(len(a_string)):
        if a_string[i] == c_string[i] or b_string[i] == c_string[i]:

            pass
        else:
            print("NO")
            break
    else:
        print("YES")
