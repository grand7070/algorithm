import sys
from collections import deque
n = int(sys.stdin.readline())
data = [0 for _ in range(n+1)]

queue = deque([n])

while queue:
    t = queue.popleft()
    if t % 3 == 0 and data[t // 3] == 0:
        data[t // 3] = data[t] + 1
        queue.append(t // 3)
    if t % 2 == 0 and data[t // 2] == 0:
        data[t // 2] = data[t] + 1
        queue.append(t // 2)
    if t - 1 > 0 and data[t - 1] == 0:
        data[t - 1] = data[t] + 1
        queue.append(t - 1)
print(data[1])