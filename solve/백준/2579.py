# 2579 계단
# 실버 3

n = int(input())
steps = [int(input()) for _ in range(n)]
dp = [0 for _ in range(n + 1)]

if n <= 2:
   print(sum(steps))

else:
  dp[1],dp[2] = steps[0], steps[0] + steps[1]
  for i in range(3, n + 1):
        dp[i] = max ((dp[i - 2] + steps[i - 1]), (dp[i - 3] + steps[i-2] + steps[i-1]))
  print(dp[n])
