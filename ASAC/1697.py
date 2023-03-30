import sys
from collections import deque

input = sys.stdin.readline
n, k = map(int, input().split())
visited = [0] * (100000 + 1)

def bfs():
    q = deque([n])
    
    while q:
        x = q.popleft()
        if x == k:
            print(visited[x])
            break
        
        for i in (x - 1, x + 1, x * 2):
            if 0 <= i <= 100000 and visited[i] == 0:
                visited[i] = visited[x] + 1
                q.append(i)

bfs()
