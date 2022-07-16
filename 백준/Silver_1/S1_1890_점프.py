import sys
n = int(sys.stdin.readline())

data = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dp = [[0]*n for _ in range(n)]

dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if [i, j] == [n-1, n-1]: break
        if dp[i][j]:
            d = data[i][j]
            if j+d < n:
                dp[i][j+d] += dp[i][j]
            if i+d < n:
                dp[i+d][j] += dp[i][j]

print(dp[n-1][n-1])