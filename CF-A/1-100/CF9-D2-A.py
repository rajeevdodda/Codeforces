# https://codeforces.com/contest/9/problem/A
max_num = max(list(map(int, input().split())))
if max_num == 6:
    print("1/6")
elif max_num == 5:
    print("1/3")
elif max_num == 4:
    print("1/2")
elif max_num == 3:
    print("2/3")
elif max_num == 2:
    print("5/6")
elif max_num == 1:
    print("1/1")