# 8979 올림픽
# 실버 5

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
data.sort(key = lambda x:(-x[1],-x[2],-x[3]))

# 리스트의 특정 열에서 원하는 값을 만족하는 index 구하기
idx = [data[i][0] for i in range(n)].index(k)
for i in range(n):
	# 등수를 구하려는 나라와 메달 현황이 같은 곳 찾으면 그 곳 index + 1 이 등수
	if data[idx][1:] == data[i][1:]:
		print(i+1)
		break