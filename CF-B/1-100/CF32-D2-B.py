# https://codeforces.com/problemset/problem/32/B


stack = list()
ans = ""
for i in input():
    if not stack:
        if i == ".":
           ans += "0"
        else:
            stack.append(i)
    else:
        if i == ".":
            ans += "1"
        else:
            ans += "2"
        stack.pop()

print(ans)

