# 2961 도영이가 만든 맛있는 음식
# 실버 2

n = int(input())
foods = [list(map(int, input().split(" "))) for _ in range(n)]
ans = [abs(i[0] - i[1]) for i in foods]