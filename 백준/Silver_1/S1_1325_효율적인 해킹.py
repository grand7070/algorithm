import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
data = {i:[] for i in range(1, n+1)}
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    data[b].append(a)
ans = 0
answer = []
for i in range(1, n+1):
    queue = deque([i])
    visit = [0]*(n+1)
    visit[i] = 1
    num = 1
    while queue:
        a = queue.popleft()
        for j in data[a]:
            if not visit[j]:
                visit[j] = 1
                queue.append(j)
                num += 1
    if num > ans:
        answer = [i]
        ans = num
    elif num == ans:
        answer.append(i)
print(*answer)