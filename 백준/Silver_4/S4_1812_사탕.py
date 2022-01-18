import sys
from collections import deque
n = int(sys.stdin.readline())
queue = deque()
for _ in range(n):
    queue.append(int(sys.stdin.readline()))
queue.append(queue.popleft())
total = sum(queue)//2
for i in range(n):
    answer = total
    for j in range(n//2):
        answer -= queue[2*j]
    print(answer)
    queue.rotate(-1)