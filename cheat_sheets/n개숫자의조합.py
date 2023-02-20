# 백트레킹(dfs)를 이용하거나 permutation 메소드 이용
# 예시는 백준 10819 풀이

n = int(input())
arr = list(map(int, input().split()))
visited = [0] * n
res = []
temp = []

def dfs(depth):
    if depth == n:
        res.append(sum(abs(temp[i] - temp[i - 1]) for i in range(n - 1)))
        return
    for i in range(n):
        if visited[i]:
            continue
        temp.append(arr[i])
        visited[i] = 1
        dfs(depth + 1)
        visited[i] = 0
        temp.pop()

dfs(0)
print(max(res))

# 조합 이용한 코드
from itertools import permutations
cases = permutations(arr)
for case in cases:
    res.append(sum(abs(case[i] - case[i - 1]) for i in range(n - 1)))
print(max(res))