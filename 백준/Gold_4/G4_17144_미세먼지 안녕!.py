import sys
r, c, t = map(int, sys.stdin.readline().split())
data = []
machine = []
for i in range(r):
    row = list(map(int, sys.stdin.readline().split()))
    if -1 in row:
        machine.append(i)
    data.append(row)

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

while t > 0:
    plus = [[0]*c for _ in range(r)]
    minus = [[0]*c for _ in range(r)]
    for y in range(r):
        for x in range(c):
            if data[y][x] > 0:
                for i in range(4):
                    ty = y + dy[i]
                    tx = x + dx[i]
                    if 0 <= ty < r and 0 <= tx < c and data[ty][tx] >= 0:
                        plus[ty][tx] += data[y][x] // 5
                        minus[y][x] += data[y][x] // 5
    # 미세먼지 정산
    for y in range(r):
        for x in range(c):
            data[y][x] += plus[y][x]
            data[y][x] -= minus[y][x]

    # 공기청정기
    data[machine[0]-1][0] = 0
    for i in range(machine[0]-1, 0, -1): # 아래
        data[i][0] = data[i-1][0]
    for i in range(c-1): # <-
        data[0][i] = data[0][i+1]
    for i in range(machine[0]): # ^
        data[i][c-1] = data[i+1][c-1]
    for i in range(c-1, 1, -1): # ->
        data[machine[0]][i] = data[machine[0]][i-1]
    data[machine[0]][1] = 0

    data[machine[1]+1][0] = 0
    for i in range(machine[1]+1, r-1): # ^
        data[i][0] = data[i+1][0]
    for i in range(c-1): # <-
        data[r-1][i] = data[r-1][i+1]
    for i in range(r-1, machine[1], -1): # 아래
        data[i][c-1] = data[i-1][c-1]
    for i in range(c-1, 1, -1): # ->
        data[machine[1]][i] = data[machine[1]][i-1]
    data[machine[1]][1] = 0
    t -= 1

ans = 0
for i in range(r):
    for j in range(c):
        ans += data[i][j]
print(ans+2)