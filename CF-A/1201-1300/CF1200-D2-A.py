# https://codeforces.com/problemset/problem/1200/A

n = int(input())

rooms = ["0"] * 10


def fill_left():
    left_pointer = 0
    while left_pointer < n:
        if rooms[left_pointer] == "0":
            rooms[left_pointer] = "1"
            break
        left_pointer += 1


def fill_right():
    right_pointer = 9
    while right_pointer > -1:
        if rooms[right_pointer] == "0":
            rooms[right_pointer] = "1"
            break
        right_pointer -= 1


for i in input():
    if i == "L":
        fill_left()
    elif i == "R":
        fill_right()
    else:
        rooms[int(i)] = "0"

print("".join(rooms))
