# 1780 종이의 개수
# 실버 2
import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
result = [0, 0, 0]

def solution(x, y, n):
    number = graph[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if graph[i][j] != number:
                for k in range(3):
                    for l in range(3):
                        solution(x + k * n // 3, y + l * n // 3, n // 3)
                return
            
    if number == -1:
        result[0] += 1
    elif number == 0:
        result[1] += 1
    else:
        result[2] += 1

solution(0, 0, n)
for i in result:
    print(i)