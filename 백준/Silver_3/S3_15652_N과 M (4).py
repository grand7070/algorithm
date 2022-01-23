import sys
from itertools import combinations_with_replacement
n, m = map(int, sys.stdin.readline().split())
data = list(combinations_with_replacement([x for x in range(1, n+1)], m))
for i in data:
    print(*i)