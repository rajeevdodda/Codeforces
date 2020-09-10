# https://codeforces.com/contest/266/problem/A
n = int(input())
colours = input()
colours_2 = list()
colours_2.append(colours[0])
ans = 0

for i in colours[1:]:
    if colours_2[-1] != i:
        colours_2.append(i)
    else:
        ans += 1
print(ans)