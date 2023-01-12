N, M = map(int, input().split())

graph = [list(map(int, input())) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y):
	if x < 0 or x >= N or y < 0 or y >= M:
		return False
	if graph[x][y] == 0:
		graph[x][y] = 1
		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i] 
			dfs(nx, ny)
		return True
	# graph[x][y]가 0이 아니면 False 반환
	return False

count = 0
for i in range(N):
	for j in range(M):
		if dfs(i, j) == True:
			count += 1

print(count)