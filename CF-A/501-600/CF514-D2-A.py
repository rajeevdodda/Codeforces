x = list(input())
ans = ""
j = 0
for i in x:
    if int(i) > 4:
        if j == 0 and int(i) == 9:
            ans += i

        else:
            ans += str(9 - int(i))
    else:
        ans += i
    j += 1

print(ans)
