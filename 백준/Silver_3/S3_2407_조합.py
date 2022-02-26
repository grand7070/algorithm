import sys
n, m = map(int, sys.stdin.readline().split())
def fact(n):
    tmp = 1
    for i in range(1, n+1):
        tmp *= i
    return tmp
print(int(fact(n)//(fact(m)*fact(n-m))))