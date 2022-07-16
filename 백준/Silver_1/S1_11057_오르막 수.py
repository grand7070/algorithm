import sys

n = int(sys.stdin.readline())

dp = [[0]*10 for _ in range(n)]

dp[0] = [1 for _ in range(10)]

if n > 1:
    for i in range(1, n):
        dp[i][0] = dp[i-1][0]
        for j in range(1, 10):
            for k in range(j+1):
                dp[i][j] += dp[i-1][k]

print(sum(dp[n-1]) % 10007)