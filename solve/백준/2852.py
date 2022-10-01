import sys

input = sys.stdin.readline

n = int(input().rstrip())
score = {1:0, 2:0}
time = {1:0, 2:0} # 골을 넣은 시간 기록용
ans = {1:0, 2:0} # 총 이기고 있던 시간
state = 0 #0 동점 1 1팀승리 2 2팀승리 

for _ in range(n):
	team, goal_time = input().split()
	team = int(team)
	m, s = map(int, goal_time.split(':'))
	t = m * 60 + s
	score[team] += 1

	if state == 0: # 동점이었는데 누군가 득점 한 경우
		time[team] = t
		state = team
	elif state != 0 and score[1] == score [2]: # 동점 아니었는데 동점된 경우
		ans[state] += t-time[state] # 이기고 있었던 팀의 시간 기록
		state = 0

if state != 0: # 전부 입력받은 후, 동점이 아니라면
	ans[state] += 60 * 48 - time[state] # 마지막에 이기고 있던 팀 기록 추가

print('{:0>2}:{:0>2}'.format(ans[1]//60, ans[1] % 60))
print('{:0>2}:{:0>2}'.format(ans[2]//60, ans[2] % 60))
# '{인덱스0}, {인덱스1}'.format(값0, 값1)
# 0>2 두칸 크기의 공간에 입력받은 값을 오른쪽 정렬하고, 빈 곳에 0을 채워넣음