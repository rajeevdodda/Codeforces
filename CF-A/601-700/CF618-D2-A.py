# https://codeforces.com/problemset/problem/618/A

n = int(input())

stack = [1]

for i in range(1, n):
    if stack[-1] == 1:
        stack[-1] = 2
        while True:
            if len(stack) >= 2:
                last = stack.pop()
                if stack[-1] == last:
                    stack[-1] = last + 1
                else:
                    stack.append(last)
                    break
            else:
                break
    else:
        stack.append(1)
print(*stack)
