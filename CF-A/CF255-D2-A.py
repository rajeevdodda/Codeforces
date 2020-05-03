# https://codeforces.com/contest/255/problem/A

n = int(input())

exercises = tuple(map(int, input().split()))
i = 0
chest, biceps, back = 0, 0, 0

while True:
    if i < n:
        chest += exercises[i]
    else:
        break

    if i + 1 < n:
        biceps += exercises[i + 1]
    else:
        break
    if i + 2 < n:
        back += exercises[i + 2]
    else:
        break
    i += 3
    #print(i)

#print(chest, biceps, back)
max_value = max(chest, biceps, back)

if max_value == chest:
    print("chest")
elif max_value == biceps:
    print("biceps")
else:
    print("back")
