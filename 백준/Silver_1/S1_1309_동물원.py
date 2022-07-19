import sys

n = int(sys.stdin.readline())

data = [[0]*3 for _ in range(n)]
data[0] = [1, 1, 1]

if n == 1 :
    print(sum(data[0]))
else:
    for i in range(1, n):
        data[i][0] = (data[i-1][1] + data[i-1][2]) % 9901# 왼쪽 위치
        data[i][1] = (data[i-1][0] + data[i-1][2]) % 9901# 오른쪽 위치
        data[i][2] = (data[i-1][0] + data[i-1][1] + data[i-1][2]) % 9901 # 배치 안함

    print(sum(data[n-1]) % 9901)