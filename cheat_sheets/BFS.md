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

### 변형

#### 백준 1260

정점의 개수 N, 간선의 개수 M, 탐색 시작할 정점의 번호 V가 주어지고 간선이 연결하는 두 노드에 대한 정보를 배열로 받았을 때. 두 정점 사이에는 여러개 간선이 있을 수 있고, 간선의 방향은 양방향이다. 방문할 수 있는 정점이 여러개인 경우에는 정점 번호가 작은 것을 먼저 방문하도록 구현

```python
import sys
from collection import deque

def dfs(n):
	visited[n] = True
	print(n, end= ' ')
	for i in graph[n]:
		if not visited[i]:
			dfs(i)

def bfs(n):
	queue = deque([n])
	visited[n] = True
	while queue:
		v = queue.popleft()
		print(v, end= ' ')
		for i in graph[v]:
			if not visited[i]:
				queue.append(i)
				visited[i] =  True

n, m, v = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)]
for i in range(m):
	a, b = map(int, sys.stdin.readline().split())
	graph[a].append(b)
	graph[b].append(a)

visited = [False] * (n + 1)
dfs(v)
print()
visited = [False] * (n + 1)
bfs(v)
```
