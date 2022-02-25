import sys
from collections import Counter
case = int(sys.stdin.readline())
for _ in range(case):
    n = int(sys.stdin.readline())
    tmp = []
    for i in range(n):
        tmp.append(sys.stdin.readline().rstrip().split()[1])
    answer = 1
    for i in list(Counter(tmp).values()):
        answer *= (i+1)
    print(answer-1)