# 1012 유기농배추
# 실버 2

import sys
from collections import deque

def bfs():
	count = 0
	queue = deque([])

	for i in range(M):
		for j in range(N):

			if graph[i][j] == 1:
				queue.append((i, j))

				while queue:
					x, y = queue.popleft()
					graph[x][y] = 0

					for k in range(4):
						nx = x + dx[k]
						ny = y + dy[k]
						if 0 <= nx < M and 0 <= ny < N and graph[nx][ny] == 1:
							graph[nx][ny] = 0 
							queue.append((nx, ny))

				count += 1

	return(count)

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

T = int(input().rstrip())

for _ in range(T):
	M, N, K = map(int, input().split(" "))

	graph = [[0] * N for _ in range(M)]

	for _ in range(K):
		a, b = map(int, input().split(" "))
		graph[a][b] = 1
	
	print(bfs())
