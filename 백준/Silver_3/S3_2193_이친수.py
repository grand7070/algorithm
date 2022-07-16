import sys

n = int(sys.stdin.readline())

d = [[0,0] for _ in range(n)]
d[0] = [0,1]

if n == 1: print(1)
else:
    for i in range(1, n):
        d[i][0] = d[i-1][0] + d[i-1][1] # 0
        d[i][1] = d[i-1][0] # 1
    print(d[n-1][0] + d[n-1][1])