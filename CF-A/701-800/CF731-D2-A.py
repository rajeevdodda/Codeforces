# https://codeforces.com/contest/731/problem/A

string = input()
alphabets = 'abcdefghijklmnopqrstuvwxyz'
pointer = 0
front = rear = pointer
ans = 0
steps = 0

for i in string:

    while True:
        if alphabets[front] == i:
            ans += steps
            steps = 0
            pointer = alphabets.find(i)
            break
        elif alphabets[rear] == i:
            ans += steps
            steps = 0
            pointer = alphabets.find(i)
            break
        else:
            front = front + 1
            front = front % 26
            rear -= 1
            steps += 1
    front = rear = pointer

print(ans)

