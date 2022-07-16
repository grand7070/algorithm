import sys
from collections import defaultdict

n = int(sys.stdin.readline())

data = defaultdict(int)
for _ in range(n):
    data[sys.stdin.readline().rstrip()] += 1

max_num = max(data.values())

candidate = []

for k, v in data.items():
    if v == max_num:
        candidate.append(k)

candidate.sort()
print(candidate[0])