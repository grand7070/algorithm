import sys

n = int(sys.stdin.readline())

a, b = 1, 2

if n == 1: print(a)
elif n == 2: print(b)
else:
    for _ in range(2, n):
        a, b = b, a + b
    print(b % 10007)
