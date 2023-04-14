n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())
visited = [[False] * n for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(x, y):
    if visited[x][y] == True:
        return
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y

        if 0 <= nx < r and 0 <= ny < c and visited[nx][ny] == False:
            visited[nx][ny] = True
            if graph[nx][ny] < graph[r - 1][c - 1]:
                graph[nx][ny] = 0
            dfs(nx, ny)

if graph[0][0] < graph[r-1][c-1]:
    graph[0][0] = 0
    
dfs(0, 0)

for i in range(n):
    for j in range(n):
        print(graph[i][j], end=" ")
    print()