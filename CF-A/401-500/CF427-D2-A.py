# https://codeforces.com/contest/427/problem/A
n = int(input())
crimes_list = map(int, input().split())
crimes = 0
temp = 0
for i in crimes_list:
    if temp <= 0 and i == -1:
        crimes += 1
    else:
        temp += i
print(crimes)




