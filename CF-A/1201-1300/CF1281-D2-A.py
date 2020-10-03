# https://codeforces.com/problemset/problem/1281/A

for _ in range(int(input())):
    string = input()
    if string[-2::1] == "po":
        print("FILIPINO")
    elif string[-4::1] == "desu" or string[-4::1] == "masu":
        print("JAPANESE")
    else:
        print("KOREAN")
