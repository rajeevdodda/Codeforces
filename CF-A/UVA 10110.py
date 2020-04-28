# https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1051
import math
while True:
    n = int(input())
    if n == 0:
        break
    x = math.sqrt(n)
    if x % 1 == 0:
        print("yes")
    else:
        print("no")
