import sys
a, b, c = map(int, sys.stdin.readline().split())

def fun(b):
    if b == 1: return a % c
    tmp = fun(b//2)
    if b % 2: # 홀수 일때
        return (( ( ((tmp % c) * (tmp % c)) % c) % c) * (a % c)) % c
    else:
        return ((tmp % c) * (tmp % c)) % c

print(fun(b))