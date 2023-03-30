import sys
from collections import deque

input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = [[0] * (m + 1) for _ in range(n + 1)]
visited = [[0] * (m + 1) for _ in range(n + 1)]

for _ in range(k):
    a, b = map(int, input().split())
    graph[a][b] = 1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(i, j):
  q = deque([(i, j)])
  cnt = 1

  while q:
      x, y = q.popleft()
      visited[x][y] = 1

      for i in range(4):
          nx = dx[i] + x
          ny = dy[i] + y

          if 1 <= nx <= n and 1 <= ny <= m and graph[nx][ny] == 1 and visited[nx][ny] == 0:
              q.append((nx, ny))
              visited[nx][ny] = 1
              cnt += 1

  return cnt

ans = -1e9
for i in range(1, n + 1):
    for j in range(1, m + 1):
      if visited[i][j] == 0 and graph[i][j] == 1:
         ans = max(ans, bfs(i, j))

print(ans)