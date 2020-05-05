# https://codeforces.com/contest/384/problem/A
import math

n = int(input())
print((math.ceil(n / 2) ** 2) + (n // 2) ** 2)
even = ""
odd = ""

for j in range(n):
    if j % 2 == 0:
        even += "C"
        odd += "."
    else:
        even += "."
        odd += "C"

for i in range(n):
    if i % 2 == 0:
        print(even)
    else:
        print(odd)
