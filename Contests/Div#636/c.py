t = int(input())

for i in range(t):
    n = int(input())
    seq_a = list(map(int, input().split()))
    stack = list()
    stack.append(seq_a[0])
    for k in range(1, n):
        if seq_a[k] > 0:
            if stack[-1] > 0:
                if stack[-1] < seq_a[k]:
                    stack.pop()
                    stack.append(seq_a[k])
            else:
                stack.append(seq_a[k])
        else:
            if stack[-1] > 0:
                stack.append(seq_a[k])
            else:
                if stack[-1] < seq_a[k]:
                    stack.pop()
                    stack.append(seq_a[k])

    print(sum(stack))
