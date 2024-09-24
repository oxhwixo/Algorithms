N, M = map(int, input().split())

array = [list(map(int, input().split())) for _ in range(N)]

result = -1e9
for i in range(N):
	result = max(result, min(array[i]))

print(result)
