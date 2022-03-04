import sys
from itertools import combinations
n, s = map(int, sys.stdin.readline().split())
data = [int(x) for x in sys.stdin.readline().split()]
cnt = 0
for i in range(1, len(data)+1):
    tmp = list(combinations(data, i))
    for i in tmp:
        if sum(i) == s:
            cnt += 1
print(cnt)