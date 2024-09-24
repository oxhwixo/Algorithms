# 12865 평범한 배낭
# 골드 5

# 냅색 알고리즘
# 백팩 안에 넣을 물건이 나눠담을 수 있는지 없는지에 따라 나뉜다.
# 물건이 나누어지면 분할가능 배낭문제(Fractional Knapsack Problem)
# 물건이 나누어지지 않으면 0-1 배낭문제(0-1Knapsack Problem)

# n번째 물건까지 살펴보았을 때, 무게가 k인 배낭의 최대가치를 dp배열에 저장

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
items = [[0, 0]]
d = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(n):
    items.append(list(map(int, input().split())))

for item in range(1, n + 1):
    for capacity in range(1, k + 1):
        weight = items[item][0]
        value = items[item][1]

        if capacity < weight:
            d[item][capacity] = d[item - 1][capacity]
        else:
            d[item][capacity] = max(d[item - 1][capacity], d[item - 1][capacity - weight] + value)
            # 이전 물건 값 그대로 OR
            # 물건을 넣은 뒤 남은 무게를 채울 수 있는 최대값 + 이번 물건 값

print(d[n][k])