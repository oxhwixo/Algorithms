# 1027 고층 건물
# 골드 4

# 그래프의 기울기를 이용한 문제
# 우측 : 현재까지 탐색한 건물 사이의 기울기의 최댓값보다 기울기가 크면 "볼 수 있는 건물"
# 좌측 : 현재까지 탐색한 건물 사이의 기울기의 최솟값보다 기울기가 작으면 "볼 수 있는 건물"

import sys
input = sys.stdin.readline

def find_slope(x1, y1, x2, y2):
    return (y2 - y1) / (x2 - x1)

n = int(input())
data = list(map(int, input().split()))
ans = 0

for target_x, target_y in enumerate(data):
    count = 0
    left_max = float(1e9)
    right_max = -float(1e9)
    
    for i in range(target_x - 1, -1, -1):
        slope = find_slope(target_x + 1, target_y, i + 1, data[i])
        if slope < left_max:
            left_max = slope
            count += 1
    for i in range(target_x + 1, n):
        slope = find_slope(target_x + 1, target_y, i + 1, data[i])
        if slope > right_max:
            right_max = slope
            count += 1
    ans = max(ans, count)

print(ans)