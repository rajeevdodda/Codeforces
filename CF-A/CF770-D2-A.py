# https://codeforces.com/contest/770/problem/A

n, k = map(int, input().split())

alphabets = "abcdefghijklmnopqrstuvwxyz"

print((alphabets[:k])*(n//k)+alphabets[:n%k])


