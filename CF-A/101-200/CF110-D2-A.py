# https://codeforces.com/contest/110/problem/A

# string = input()
# lucky = 0

# for i in string:
#     if i in "47":
#         lucky += 1

# if lucky == 4 or lucky == 7:
#     print("YES")
# else:
#     print("NO")


n = int(input())
lucky = 0
while n > 0:
    temp = n % 10
    n = n // 10

    if temp == 4 or temp == 7:
        lucky += 1


if lucky == 4 or lucky == 7:
    print("YES")
else:
    print("NO")