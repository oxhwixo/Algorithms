# 나머지 연산을 이용하기
# 음수의 나머지 연산에 주의할 것

def turn(direction, c):
	if c == "L":
		# -1 % 4 = 몫 -1 나머지 3 (-4 + 3 = -1)
		direction = (direction - 1) % 4 
	else:
		direction = (direction + 1) % 4
	return direction 