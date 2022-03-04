import sys
n, a, b = map(int, sys.stdin.readline().split())

def fun(x):
    return (x+1)//2 if x % 2 else x//2

ans = 1
while True:
    a, b = fun(a), fun(b)
    if a == b: break
    ans += 1

print(ans)