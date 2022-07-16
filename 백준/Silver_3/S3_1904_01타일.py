import sys

n = int(sys.stdin.readline())

a, b = 1, 2

if n == 1:
    print(a)
elif n > 1:
    for i in range(2, n):
        a, b = b, a + b
    print(b % 15746)