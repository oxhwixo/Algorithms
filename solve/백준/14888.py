import sys

input = sys.stdin.readline
n = int(input())
numbers = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
max_num = -1e9
min_num = 1e9

def dfs(depth, result, add, sub, mul, div):
    global min_num
    global max_num

    if depth == n:
        min_num = min(min_num, result)
        max_num = max(max_num, result)
        return
    
    if add > 0:
        dfs(depth + 1, result + numbers[depth], add-1, sub, mul, div)
    if sub > 0:
        dfs(depth + 1, result - numbers[depth], add, sub-1, mul, div)
    if mul > 0:
        dfs(depth + 1, result * numbers[depth], add, sub, mul-1, div)
    if div > 0:
        dfs(depth + 1, int(result / numbers[depth]) , add, sub, mul, div-1)
 
dfs(1, numbers[0], add, sub, mul, div)
print(max_num)
print(min_num)