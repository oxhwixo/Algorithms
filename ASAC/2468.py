import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
graph = []
for _ in range(n):
	graph.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, h):
	queue = deque([(x, y)])
	while queue:
		x, y = queue.popleft()
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]

			if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and graph[nx][ny] > h:
				visited[nx][ny] = True
				queue.append((nx, ny))

result = 0
for k in range(max(map(max,graph))):
	visited = [[False] * n for _ in range(n)]
	count = 0
	for i in range(n):
			for j in range(n):
				if graph[i][j] > k and not visited[i][j]:
					count += 1
					visited[i][j] = True
					bfs(i, j, k)
	result = max(result, count)

print(result)