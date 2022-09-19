# 11399 ATM
# 실버 4

n = int(input())
data = list(map(int, input().split()))

data.sort()

res = 0
for i in range(n):
	res = data[i] * (n - i) + res


print(res)