# 1009 분산처리
# 브론즈 2

n = int(input())
data = []

#	number = int((a ** b) % 10) 제곱해서 하면 시간초과뜸
# 밑수 1의 자리에 규칙이 있음

for _ in range(n):
	a, b = map(int, input().split(" "))
	base = a % 10

	if base == 0:
		print(10)
	elif base in [1, 5, 6]:
		print(base)
	elif base in [4, 9]:
		base2 = b % 2
		if base2 == 0:
			print(base * base % 10)
		else:
			print(base)
	else:
		base2 = b % 4
		if base2 == 0:
			print(base ** 4 % 10)
		else:
			print(base ** base2 % 10)
