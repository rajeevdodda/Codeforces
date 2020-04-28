t = int(input())

for i in range(t):
    n, a, b = map(int, input().split())
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    print((n // b) * alphabets[:b] + alphabets[:n % b])
