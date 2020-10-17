# https://codeforces.com/problemset/problem/735/A

n, k = map(int, input().split())

T_index = None
G_index = None

l = 0
string = input()
for i in string:
    if i == "T" or i == "G":
        break
    l += 1

for i in range(l + k, n, k):

    if string[i] == "T" or string[i] == "G":
        print("YES")
        break
    elif string[i] == "#":
        print("NO")
        break
else:
    print("NO")
