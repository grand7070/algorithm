import sys
from itertools import combinations_with_replacement
n, m = map(int, sys.stdin.readline().split())
tmp = sorted(list(map(int, sys.stdin.readline().split())))
results = list(combinations_with_replacement((tmp), m))
for result in results:
	print(*result)