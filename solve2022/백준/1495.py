# 1495 기타리스트
# 실버 1

import sys
input = sys.stdin.readline

n, s, m = map(int, input().split())
v = list(map(int, input().split()))

# [곡 순서][볼륨] = 가능(=1) / 불가능(=0)
d = [[0] * (m + 1) for _ in range(n + 1)]
d[0][s] = 1

for i in range(1, n + 1):
    for j in range(m + 1):
        if d[i - 1][j] == 1:
            if 0 <= (j + v[i-1]) <= m:
                d[i][j + v[i - 1]] = 1
            if 0 <= (j - v[i - 1]) <=m:
                d[i][j - v[i - 1]] = 1

ans = -1
for i in range(m, -1, -1):
    if d[n][i] == 1:
        ans = i
        break

print(ans)