# https://codeforces.com/contest/431/problem/A
calories = input().split()
calories_dict = {key: value for key, value in enumerate(calories, start=1)}

string = input()
ans = 0
for i in string:
    ans += int(calories_dict.get(int(i)))

print(ans)
