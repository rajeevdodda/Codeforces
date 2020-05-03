# https://codeforces.com/contest/454/problem/A

n = int(input())

j = 1
i = n // 2
k = 0
while k < n:
    if k < n //2:
        print("*"*i+"D"*j+"*"*i)
        j += 2
        i -= 1
        if j > n:
            j -= 2
            i += 1
    else:
        print("*" * i + "D" * j + "*" * i)
        j -= 2
        i += 1
    k += 1

