import sys
from collections import deque

def bfs(x, y):
  queue = deque([(x, y)])
  
  while queue:
    x, y = queue.popleft()
    if x == nodes[1][0] and y == nodes[1][1]:
      print(graph[x][y])
      break
    
    for i in range(8):
      nx = x + dx[i]
      ny = y + dy[i]
      
      if 0 <= nx < size and 0 <= ny < size and graph[nx][ny] == 0:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx, ny))

input = sys.stdin.readline
n = int(input())
for _ in range(n):
    size = int(input())
    graph = [[0] * size for _ in range(size)]
    nodes = [list(map(int, input().split())) for _ in range(2)]

    dx = [-1, -2, -2, -1, 1, 2, 2, 1]
    dy = [-2, -1, 1, 2, 2, 1, -1, -2]

    bfs(nodes[0][0], nodes[0][1])