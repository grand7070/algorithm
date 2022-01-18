import sys
n, m = map(int, sys.stdin.readline().split())
a, b = 1001, 1001
for _ in range(m):
    package, piece = map(int, sys.stdin.readline().split())
    a, b = min(package, a), min(piece, b)
print(min(a*(n//6)+b*(n%6), a*(n//6+1)), b*n)