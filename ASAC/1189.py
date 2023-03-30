import sys
input = sys.stdin.readline

r, c, k = map(int, input().split())
graph = [list(input().strip()) for _ in range(r)]
visited = [[0] * c for _ in range(r)]
cnt = 0

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bt(depth, x, y):
    global cnt
    if depth == k:
        if x == 0 and y == c - 1:
            cnt += 1
        return
    
    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y

        if 0 <= nx < r and 0 <= ny < c and graph[nx][ny] == '.' and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            bt(depth + 1, nx, ny)
            visited[nx][ny] = 0

visited[r - 1][0] = 1
bt(1, r - 1, 0) 
print(cnt)
