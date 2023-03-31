import sys
from collections import deque

input = sys.stdin.readline

f, s, g, u, d = map(int, input().split())
visited = [0] * (f + 1)

def bfs():
    
  q = deque([s])
  visited[s] = 1
  while q:
      x = q.popleft()
      if x == g:
         print(visited[g] - 1)
         return
      
      if 0 < x + u <= f and visited[x + u] == 0:
         visited[x + u] = visited[x] + 1
         q.append(x + u)
      if 0 < x - d <= f and visited[x - d] == 0:
         visited[x - d] = visited[x] + 1
         q.append(x - d)

  print("use the stairs")

bfs()