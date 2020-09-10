# https://codeforces.com/contest/721/problem/A
n = int(input())
string = input()

blacks_list = list()
ans = 0
for i in string:
    if i == "B":
        ans += 1
    else:
        if ans != 0:
            blacks_list.append(ans)
        ans = 0
if ans:
    blacks_list.append(ans)

print(len(blacks_list))
print(*blacks_list)
