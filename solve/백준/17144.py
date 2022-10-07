# 17144 미세먼지 안녕!
# 골드 4

import sys
input = sys.stdin.readline

r, c, t = map(int, input().split())
data = [list(map(int, input().split()))for _ in range(r)]
top = 0
bottom = 0

for i in range(r):
	if data[i][0] == -1 :
		top = i
		bottom = i + 1
		break

# 확산
# 인접한 네 방향으로 확산, 공기청정기가 있거나 칸이 없으면 확산 X, 동시에 일어남
# 확산되는 양은 Ar,c/5이고 소수점은 버린다.
# (r, c)에 남은 미세먼지의 양은 Ar,c - (Ar,c/5)×(확산된 방향의 개수) 이다.

def spread():
	dx = [-1, 1, 0, 0] # 상 하 좌 우
	dy = [0, 0, -1, 1]
	temp = [[0] * c for _ in range(r)] # 확산 후 결과 저장

	for x in range(r):
		for y in range(c):
			if data[x][y] == 0 or data[x][y] == -1:
				continue

			dust = data[x][y] // 5

			for i in range(4):
				nx, ny = x + dx[i], y + dy[i]
				if 0 <= nx < r and 0 <= ny < c and data[nx][ny] != -1:
					temp[nx][ny] += dust
					temp[x][y] -= dust # 0 - dust 라서 음수 값이 저장됨

	for i in range(r):
		for j in range(c):
			data[i][j] += temp[i][j]


# 공기청정기 작동
# 위쪽은 반시계 순환, 아래쪽은 시계방향 순환
# 바람이 불면 미세먼지가 바람 방향대로 한 칸씩 이동
# 공기청정기로 들어간 미세먼지는 정화됨

def clean_up():
	dx = [0, -1, 0, 1] # 우 상 좌 하 
	dy = [1, 0, -1, 0]
	x, y, direction = top, 1, 0  
	before = 0 # 공기청정기 바로 옆의 먼지가 이동하면 그 자리는 빈자리가 된다.

	while True: 
		nx, ny = x + dx[direction], y + dy[direction]
		if x == top and y == 0:
			break
		if not 0 <= nx < r or not 0 <= ny < c: # 범위를 벗어나면 방향 전환
			direction += 1
			continue
		
		# (x, y) 위치에 이 전 값을 저장하고, 이전 값은 x, y 값으로 갱신함
		data[x][y], before = before, data[x][y]
		x, y = nx, ny # x,y 값 갱신 (이동)

def clean_down():
	dx = [0, 1, 0, -1] # 우 하 좌 상
	dy = [1, 0, -1, 0]
	x, y, direction = bottom, 1, 0
	before = 0

	while True: 
		nx, ny = x + dx[direction], y + dy[direction]
		if x == bottom and y == 0:
			break
		if not 0 <= nx < r or not 0 <= ny < c:
			direction += 1
			continue
		
		data[x][y], before = before, data[x][y]
		x, y = nx, ny

for _ in range(t):
    spread()
    clean_up()
    clean_down()

# 공기청정기를 표현한 2칸이 -1로 되어있기 때문에 2를 더해줌
print(sum(map(sum, data)) + 2) 