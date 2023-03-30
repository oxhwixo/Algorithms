import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
cnt = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(n):
    visited[n] = 1

    for i in graph[n]:
        if visited[i] == 0:
          dfs(i)

for i in range(1, n + 1):
    if visited[i] == 0:
        cnt += 1
        dfs(i)

print(cnt)