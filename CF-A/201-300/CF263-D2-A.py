# https://codeforces.com/contest/263/problem/A
# x, y = 0, 0
# for i in range(1, 6):
#     row = input().split()
#     j_index = 1
#     for j in row:
#         if j == '1':
#             x = j_index
#             y = i
#             break
#         else:
#             j_index += 1
#     if x != 0 and y != 0:
#         break

# print(abs(3-x) + abs(3-y))

for i in range(5):
    row = input().split()
    c_value = 0
    ans = False
    for c in range(5):
        if row[c] == "1":
            c_value = c
            ans = True
            break
    if ans:
        print(abs(2-c_value) + abs(2-i))
        break

    

