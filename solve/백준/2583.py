import sys
sys.setrecursionlimit(10000)

input = sys.stdin.readline
m, n, k = map(int, input().split())
graph = [[0] * m for _ in range(n)] #0,0이 맨 왼쪽 위로 가게끔 돌린 것 (M = x, N = y)
for i in range(k):
    start_y, start_x, end_y, end_x = map(int, input().split())
    for x in range(start_x, end_x):
        for y in range(start_y, end_y):
            graph[y][x] = 1
ans = []

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(y, x):
    global cnt
    graph[y][x] = 1

    for i in range(4):
      ny = y + dy[i]
      nx = x + dx[i]

      if 0 <= ny < n and 0 <= nx < m and graph[ny][nx] == 0:
          graph[ny][nx] = 1
          cnt += 1
          dfs(ny, nx)

for y in range(n):
    for x in range(m):
        if graph[y][x] == 0:
            cnt = 1
            dfs(y, x)
            ans.append(cnt)

ans.sort()
print(len(ans))
for i in ans:
    print(i, end=' ')