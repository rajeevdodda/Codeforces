# https://codeforces.com/contest/474/problem/A
d = input()
if d == "L":
    j = 1
else:
    j = -1
text = input()
first_row = 'qwertyuiop'
second_row = "asdfghjkl;"
third_row = "zxcvbnm,./"
ans = ""

for i in text:
    if i in first_row:
        ans += first_row[first_row.index(i) + j]
    elif i in second_row:
        ans += second_row[second_row.index(i) + j]
    elif i in third_row:
        ans += third_row[third_row.index(i) + j]
print(ans)
