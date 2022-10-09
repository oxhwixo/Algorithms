# 16236 아기상어
# 골드 3

from collections import deque

n = int(input())
graph = [list(map(int, input().split(" "))) for _ in range(n)]

INF = 1e9

now_size = 2
now_x, now_y = 0,0

for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            now_x,now_y = i,j
            graph[now_x][now_y] = 0 # 그대로 9로 남겨두면 이 위치를 못지나감

dx = [-1,0,1,0]
dy = [0,-1,0,1]

# 아기상어가 이동가능한 위치들의 최단거리를 구하는 함수
# 아기상어가 현재 위치한 좌표를 큐에 삽입하고 인접한 네 방향 탐색
# 문제의 조건들을 모두 만족한다면 큐에 삽입

def bfs():
	dist = [[-1] * n for _ in range(n)] # 아기상어 위치는 최단거리 0
	queue = deque([(now_x, now_y)])
	dist[now_x][now_y] = 0
	while queue:
		x,y = queue.popleft()
		for i in range(4):
			nx = x+dx[i]
			ny = y+dy[i]
			if 0<=nx<n and 0<=ny<n:
				if graph[nx][ny] <= now_size and dist[nx][ny] == -1:
					queue.append((nx,ny))
					dist[nx][ny] = dist[x][y] + 1
	return dist

	# 먹을 물고기를 찾는 함수
def find(dist):
	x,y = 0,0
	min_dist = INF
	for i in range(n):
		for j in range(n):
			# 갈 수 있는 위치이고, 1 <= 물고기크기 < 상어크기인 경우
			if dist[i][j] != -1 and 1 <= graph[i][j] < now_size:
				if dist[i][j] < min_dist: # 왼쪽, 위쪽의 최소값이 제일 먼저 들어감
					x,y = i,j
					min_dist = dist[i][j]
	if min_dist == INF:
		return None
	else:
		return x,y,min_dist

result = 0
ate = 0

while True:
	value = find(bfs())
	if value == None:
			print(result)
			break
	else:
			now_x,now_y = value[0],value[1] # 현재 위치를 옮김
			result+=value[2] # 이동거리 = 이동시간
			graph[now_x][now_y] = 0 # 자기 자신의 위치는 거리 0
			ate += 1
	if ate >= now_size: # 먹은 물고기 크기 누적이 현재 사이즈보다 같거나 크면
			now_size += 1 # 물고기 크기 올려주고 
			ate = 0 # 다시 누적은 0으로 초기화 