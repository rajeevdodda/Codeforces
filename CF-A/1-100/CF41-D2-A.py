# https://codeforces.com/contest/41/problem/A
a = input()
b = input()
# if a == b[::-1]:
#     print("YES")
# else:
#     print("NO")

l = len(a) - 1 
i = 0

if len(a) != len(b):
    print("NO")

else:
    while i < len(a) and l > -1:
        if a[i] != b[l]:
            print("NO")
            break
        l -= 1
        i += 1

    else:
        print("YES")



