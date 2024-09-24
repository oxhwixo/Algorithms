#설탕 배달 실버 4

import sys

input = sys.stdin.readline
n = int(input())
result = n // 5
n = n % 5
result += n // 3
if n % 3 == 0 :
    print(result)
else:
    print(-1)