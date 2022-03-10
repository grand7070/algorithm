import sys
from collections import deque
n = int(sys.stdin.readline())
t = int(sys.stdin.readline())
data = {i:[] for i in range(1, n+1)}
for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    data[a].append(b)
    data[b].append(a)

visit = [0]*(n+1)
def bfs(start):
    queue = deque([start])
    visit[1] = 1
    answer = 0
    while queue:
        computer = queue.popleft()
        for i in data[computer]:
            if not visit[i]:
                visit[i] = 1
                answer += 1
                queue.append(i)
    return answer

print(bfs(1))