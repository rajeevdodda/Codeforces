# https://codeforces.com/contest/556/problem/A

n = int(input())
string = input()
ones = 0
zeros = 0
for i in string:
    if i == "1":
        ones += 1
    else:
        zeros += 1

print(abs(ones - zeros))
