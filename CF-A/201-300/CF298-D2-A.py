# https://codeforces.com/contest/298/problem/A

n = int(input())
string = input()
first_letter = None
first_number = 0
last_number = None

for i in range(n):
    if string[i] != ".":
        if first_letter is None:
            first_letter = string[i]
            first_number = i

if first_letter == "L":
    for j in range(first_number, n):
        if string[j] == ".":
            if last_number is None:
                last_number = j

    print(last_number, first_number)
else:
    for j in range(first_number, n):
        if string[j] == "L":
            last_number = j
            break
        if string[j] == ".":
            if last_number is None:
                last_number = j
                break
    print(first_number + 1, last_number + 1)
