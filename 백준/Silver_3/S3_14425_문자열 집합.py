import sys
n, m = map(int, sys.stdin.readline().split())
data = [sys.stdin.readline().rstrip() for _ in range(n)]
s = [sys.stdin.readline().rstrip() for _ in range(m)]
data = set(data)
s = set(s)
print(len(s) - len(s - data))