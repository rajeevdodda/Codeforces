# # https://codeforces.com/problemset/problem/1209/A
#
# def is_prime(number):
#     for i in range(2, number):
#         if (number % i) == 0:
#             return False
#     return True
#
#
# primes = list()
#
# non_primes = list()
#
# n = int(input())
#
# for number in map(int, input().split()):
#     if number != 1:
#         if is_prime(number):
#             primes.append(number)
#         else:
#             non_primes.append(number)
#
#

n = int(input())

numbers = sorted(map(int, input().split()))
count = 0
ans = set()
for i in range(n):
    if numbers[i] is not None:
        for j in range(i + 1, n):
            if numbers[j] is not None:
                if numbers[j] % numbers[i] == 0:
                    numbers[j] = None
                    count += 1
                    ans.add(numbers[i])
    if count == n:
        break
for i in numbers:
    if i is not None:
        ans.add(i)
print(len(ans))
