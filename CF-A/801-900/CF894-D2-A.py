# https://codeforces.com/problemset/problem/894/A

string = input()
ans = 0

for i in range(len(string)):
    if string[i] == "Q":
        for k in range(i+1, len(string)):
            if string[k] == "A":
                for l in range(k+1, len(string)):
                    if string[l] == "Q":
                        ans += 1
print(ans)