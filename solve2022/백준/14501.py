# 14501 퇴사
# 실버3

import sys
input = sys.stdin.readline()
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [0 for _ in range(n + 1)]

# for i in range(n):
#     for j in range(i + arr[i][0], n + 1):
#         if dp[j] < dp[i] + arr[i][1]:
#             dp[j] = dp[i] + arr[i][1]

# print(dp[-1])            

for i in range(n - 1, -1, -1):
    if i + arr[i][0] > n:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + 1], arr[i][1] + dp[i + arr[i][0]])
        # i일에 상담을 하는 것과 상담을 안하는 것 중 큰 것 선택

print(dp[0])