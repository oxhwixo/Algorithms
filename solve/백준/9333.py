# 9333 돈 갚기
# 실버 1

import sys
input = sys.stdin.readline

n = int(input())

# def my_round(number):
#   number = round(round(number, 8), 3)

#   check = (number * 1000) % 100

#   if check >= 50:
#      return round(number + 0.001, 2)
#   else:
#      return round(number, 2)

# for _ in range(n):
#   r, b, m = map(float, input().split())
#   count = 0

#   while b > 0:
#     if count > 1200:
#         count = -1
#         break
    
#     interest = my_round(b * (r / 100))
#     b = round(round(b + interest - m, 8), 2)
#     count += 1

#   print("impossible" if count == -1 else count)
