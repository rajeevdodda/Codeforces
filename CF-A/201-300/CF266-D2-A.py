# https://codeforces.com/contest/266/problem/A
# n = int(input())
# colours = input()
# colours_2 = list()
# colours_2.append(colours[0])
# ans = 0

# for i in colours[1:]:
#     if colours_2[-1] != i:
#         colours_2.append(i)
#     else:
#         ans += 1
# print(ans)


n = int(input())

colours = input()
j = 0
ans = 1
for i in range(1, n):
    if colours[i] != colours[j]:
        ans += 1
        j = i

print(n-ans)
    
