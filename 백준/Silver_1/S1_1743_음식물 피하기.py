import sys
from collections import deque

n, m, k = map(int, sys.stdin.readline().split())
data = [["." for _ in range(m)] for _ in range(n)]

for _ in range(k):
    i, j = map(int, sys.stdin.readline().split())
    data[i-1][j-1] = "#"

visit = [[0 for _ in range(m)] for _ in range(n)]

# 상 하 좌 우
dy = [1, -1, 0, 0]
dx = [0, 0, -1, 1]

answer = 0

for i in range(n):
    for j in range(m):
        if visit[i][j] == 0 and data[i][j] == "#":
            size = 1
            queue = deque([[i, j]])
            visit[i][j] = 1
            while queue:
                y, x = queue.popleft()
                for r in range(4):
                    y_ = y + dy[r]
                    x_ = x + dx[r]
                    if 0 <= y_ < n and 0 <= x_ < m and data[y_][x_] == "#" and visit[y_][x_] == 0:
                        queue.append([y_, x_])
                        visit[y_][x_] = 1
                        size += 1
            answer = max(answer, size)

print(answer)