
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n = int(input())
graph = [list(input().strip()) for _ in range(n)]
cnt_normal = 0
cnt_special = 0

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(x, y, color):
    visited[x][y] = 1

    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0 and graph[nx][ny] == color:
            visited[nx][ny] = 1
            dfs(nx, ny, color)

def dfs2(x, y, color):
    visited[x][y] = 1

    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if 0 <= nx < n and 0 <= ny < n and visited[nx][ny] == 0:
           if color == 'R' or color == 'G':
            if graph[nx][ny] == 'R' or graph[nx][ny] == 'G':
                visited[nx][ny] = 1
                dfs2(nx, ny, color)            
           elif graph[nx][ny] == color:
              visited[nx][ny] = 1
              dfs2(nx, ny, color)
    
    
visited = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            cnt_normal += 1
            dfs(i, j, graph[i][j])
            
visited = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            cnt_special += 1
            dfs2(i, j, graph[i][j])

print(cnt_normal, cnt_special)
