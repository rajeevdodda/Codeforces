# https://codeforces.com/contest/59/problem/A
# string = input()
# upper, lower = 0, 0
# for i in string:
#     if i.isupper():
#         upper += 1
#     else:
#         lower += 1
# if lower >= upper:
#     print(string.lower())
# else:
#     print(string.upper())

string = input()

upper_word = ""
lower_word = ""

upper_count = 0
lower_count = 0

for i in string:
    if i.isupper():
        upper_count += 1
        upper_word += i
        lower_word += i.lower()
    else:
        lower_count += 1
        upper_word += i.upper()
        lower_word += i

if lower_count >= upper_count:
    print(lower_word)
else:
    print(upper_word)