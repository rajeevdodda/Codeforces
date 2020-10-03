# https://codeforces.com/problemset/problem/1216/A

n = int(input())
string = input()
ans = 0
new_string = ""
for i in range(0, n, 2):
    if string[i:i+2] == "ab" or string[i:i+2] == "ba":
        new_string += string[i:i+2]
    else:
        if string[i:i+2] == "aa":
            new_string += "ab"
        else:
            new_string += "ba"
        ans += 1

if ans:

    print(ans)
    print(new_string)
else:
    print(ans)
    print(string)