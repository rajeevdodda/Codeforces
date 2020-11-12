# https://codeforces.com/problemset/problem/938/A

n = input()
s = list()
vowels = {'a', 'e', 'i', 'o', 'u', 'y'}

for i in input():
    if not s:
        s.append(i)
    else:
        if s[-1] in vowels and i in vowels:
            pass
        else:
            s.append(i)

print(''.join(s))