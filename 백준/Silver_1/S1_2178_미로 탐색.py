import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
data = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

def bfs(y, x):
    # 오른쪽, 아래, 왼쪽, 위
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    queue = deque([[y, x]])
    visited[y][x] = 1
    while queue:
        dot = queue.popleft()
        y, x = dot[0], dot[1]
        if [y, x] == [n - 1, m - 1]:
            return visited[y][x]
        for i in range(4):
            ty = y + dy[i] # 행
            tx = x + dx[i] # 열
            if 0 <= ty < n and 0 <= tx < m and data[ty][tx] and not visited[ty][tx]:
                visited[ty][tx] = visited[y][x] + 1
                queue.append([ty, tx])

print(bfs(0, 0))