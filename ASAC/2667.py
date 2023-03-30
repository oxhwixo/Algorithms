import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
graph = [list(map(int, input().strip())) for _ in range(n)]
ans = []

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(i, j):
    q = deque([(i, j)])
    cnt = 1

    while q:
        x, y = q.popleft()
        graph[x][y] = 0

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx, ny))
                cnt += 1
                
    ans.append(cnt)

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            bfs(i, j)

ans.sort()
print(len(ans))
for i in ans:
    print(i)
