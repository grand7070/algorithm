import sys
n, r, c = map(int, sys.stdin.readline().split())
ans = 0
for i in range(n, -1, -1):
    if 2**i <= r % (2**(i+1)):
        ans += (2**i)*(2**i)*2
    if 2**i <= c % (2**(i+1)):
        ans += (2**i)*(2**i)*1
print(ans)