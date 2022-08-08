## BFS 코드

### 인접 리스트 방식 이용 BFS

```python
from collections import deque

def bfs(graph, start, visited):
	queue = deque([start])
	# 현재 노드 방문 처리
	visited[start] = True
	print(v, end = ' ')
	while queue:
		# 큐가 비어질 때 까지 반복
		v = queue.popleft()
		print(v, end = ' ')
		for i in graph[v]:
			if not visited[i]:
				queue.append(i)
				visited[i] = True

	graph = [
		[],
		[2, 3, 8],
		[1, 7],
		[1, 4, 5],
		[3, 5],
		[3, 4],
		[7],
		[2, 6, 8],
		[1, 7]
	]

visited = [False] * 9

bfs(graph, 1, visited)
```
