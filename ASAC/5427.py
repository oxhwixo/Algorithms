from collections import deque
import sys

input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    q.append((x, y))
    visited[x][y] = 1

    while q:
        len_q = len(q) # 한 사이클 처리하고 fire 해야하기 때문에 
        while len_q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < h and 0 <= ny < w:
                    if graph[nx][ny] == '.' and visited[nx][ny] == 0:
                        visited[nx][ny] = visited[x][y] + 1
                        q.append((nx, ny))
                elif nx < 0 or ny < 0 or nx >= h or ny >= w:
                    print(visited[x][y])
                    return
            len_q -= 1
        fire()

    print("IMPOSSIBLE")
    return

def fire():
    len_q = len(fire_q)
    while len_q:
        x, y = fire_q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w:
                if graph[nx][ny] == '.':
                    graph[nx][ny] = '*'
                    fire_q.append([nx, ny])
        len_q -= 1

n = int(input())

for _ in range(n):
    w, h = map(int, input().split())

    graph = [list(map(str, input().strip())) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]
    
    fire_q, q = deque([]), deque([])
    
    for i in range(h):
        for j in range(w):
            if graph[i][j] == '@':
                start_x = i; start_y = j
                graph[i][j] = '.'
            if graph[i][j] == '*':
                fire_q.append((i, j))
    fire()
    bfs(start_x, start_y)