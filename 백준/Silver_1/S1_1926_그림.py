import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

visit = [[0]*m for _ in range(n)]

# 상 하 좌 우
dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

num = 0
max_size = 0

for i in range(n):
    for j in range(m):
        if not visit[i][j] and data[i][j] == 1:
            queue = deque([[i, j]])
            visit[i][j] = 1
            size = 1
            num += 1
            while queue:
                y, x = queue.popleft()
                for r in range(4):
                    ny = y + dy[r]
                    nx = x + dx[r]
                    if 0 <= ny < n and 0 <= nx < m and not visit[ny][nx] and data[ny][nx] == 1:
                        queue.append([ny, nx])
                        visit[ny][nx] = 1
                        size += 1
            max_size = max(max_size, size)

print(num)
print(max_size)