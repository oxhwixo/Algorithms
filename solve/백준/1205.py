# 1205 등수 구하기
# 실버 4
 
import sys

N,score,P=map(int,sys.stdin.readline().split())

if N==0:
	print(1)

else:
	score_list=list(map(int,sys.stdin.readline().split()))
	score_list.append(score)
	score_list.sort(reverse=True)
	list_len = len(score_list)

	# 순위 구하기
	for a in range(list_len):
		if score_list[a]==score:
			first_rank = a + 1
			break
	# 추가될 위치 구하기
	for a in range(list_len):
		if score_list[list_len - 1 - a] == score:
			last_rank = list_len - a
			break

	if last_rank > P:
		print(-1)
	else:
		print(first_rank)
