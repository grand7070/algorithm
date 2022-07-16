import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

data = [list(sys.stdin.readline().rstrip()) for _ in range(m)]

visit = [[0]*n for _ in range(m)]

w_p, b_p = 0, 0

dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

queue = deque([])

for i in range(m):
    for j in range(n):
        if not visit[i][j]:
            queue.append([i, j])
            visit[i][j] = 1
            size = 1
            team = data[i][j]
            while queue:
                y, x = queue.popleft()
                for r in range(4):
                    ny = y + dy[r]
                    nx = x + dx[r]
                    if 0 <= ny < m and 0 <= nx < n and not visit[ny][nx] and data[ny][nx] == team:
                        queue.append([ny, nx])
                        visit[ny][nx] = 1
                        size += 1
            if team == "W": w_p += size**2
            else: b_p += size**2
print(w_p, b_p)