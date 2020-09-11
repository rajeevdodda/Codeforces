# https://codeforces.com/problemset/problem/705/A

n = int(input())

a = "I hate that I love that"

if n == 1:
    print("I hate it")
elif n == 2:
    print("I hate that I love it")
else:
    for i in range(n-1):
        if i % 2 == 0:
            print("I hate that", end=" ")
        else:
            print("I love that", end=" ")
    
    if n % 2 == 1:
         print("I hate it")
    else:
        print("I love it")
