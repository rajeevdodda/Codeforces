# https://codeforces.com/problemset/problem/1367/A

t = int(input())

for i in range(t):

    string_b = input()
    n = len(string_b)

    if n == 2:
        print(string_b)
    else:
        string_a = string_b[0]
        for k in range(1, n-1, 2):
            string_a += string_b[k]
        string_a += string_b[-1]
        print(string_a)
