# 1753 최단경로
# 골드 4

import heapq
import sys
INF = int(1e9)

input = sys.stdin.readline

V, E = map(int, input().split())
start = int(input().rstrip())
graph = [[] for _ in range(V + 1)]

for _ in range(E):
	a, b, c = map(int, input().split())
	graph[a].append((b, c))

distance = [INF] * (V + 1)

def dijkstra(start):
	q = []
	heapq.heappush(q, (0, start))
	distance[start] = 0

	while q:
		dist, now = heapq.heappop(q)

		# 거리테이블에 저장된 거리가 현재 거리보다 작다면
		# 이미 해당 노드가 처리(방문)되었음을 의미한다.
		if distance[now] < dist:
			continue
		
		# 방문한 적 없는 노드라면 
		for i in graph[now]:
			# i[0] = 노드 i[1] = i[0]으로 가기위한 비용
			cost = dist + i[1]
			if cost < distance[i[0]]:
				distance[i[0]] = cost
				heapq.heappush(q, (cost, i[0]))

dijkstra(start)
for i in range(1, V + 1):
	if distance[i] == INF:
		print("INF")
	else:
		print(distance[i])
