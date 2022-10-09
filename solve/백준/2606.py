# 2606 바이러스
# 실버 3

num_of_computer = int(input())
num_of_pair = int(input())

graph = [[] for _ in range(num_of_computer + 1)]
visited = [False] * (num_of_computer + 1)

for _ in range(num_of_pair):
	a, b = map(int, input().split(" "))
	graph[a].append(b)
	graph[b].append(a)

def dfs(v):
	global count
	visited[v] = True
	for i in graph[v]:
		if visited[i] == False:
			count += 1
			dfs(i)

global count
count = 0
dfs(1)
print(count)
