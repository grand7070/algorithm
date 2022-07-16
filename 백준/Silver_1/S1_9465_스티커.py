import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    data = [list(map(int, sys.stdin.readline().split())) for _ in range(2)]
    dp = [[0]*n for _ in range(2)]

    dp[0][0], dp[1][0] = data[0][0], data[1][0]
    for i in range(1, n):
        dp[0][i] = max(data[0][i] + dp[1][i-1], dp[0][i-1])
        dp[1][i] = max(data[1][i] + dp[0][i-1], dp[1][i-1])
    print(max(dp[0][n-1], dp[1][n-1]))