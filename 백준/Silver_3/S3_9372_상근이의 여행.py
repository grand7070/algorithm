import sys
from collections import deque
t = int(sys.stdin.readline())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    data = {i:[] for i in range(1, n+1)}
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        data[a].append(b)
        data[b].append(a)

    num = 0
    queue = deque([1])
    visited = [1]
    while queue:
        a = queue.popleft()
        for i in data[a]:
            if i not in visited:
                num += 1
                queue.append(i)
                visited.append(i)
    print(num)