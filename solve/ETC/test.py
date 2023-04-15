graph = [list(map(int, input().split())) for _ in range(8)]
dp = [[0] * 8 for _ in range(8)]
dp[0][0] = graph[0][0]

for i in range(1,8):
    dp[0][i] = dp[0][i-1] + graph[0][i]
    dp[i][0] = dp[i-1][0] + graph[i][0]

for i in range(1, 8):
    for j in range(1, 8):
        dp[i][j] = max(dp[i-1][j] + graph[i][j], dp[i][j-1] + graph[i][j])

print(dp[7][7])