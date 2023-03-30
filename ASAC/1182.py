import sys
input = sys.stdin.readline

n, s = map(int, input().split())
datas = list(map(int, input().split()))

ans = 0

def bt(depth, sum):
    global ans

    if depth >= n:
        return 
    sum += datas[depth]
    if sum == s:
        ans += 1
    
    bt(depth + 1, sum) # 자기 자신을 포함하는 경우
    bt(depth + 1, sum - datas[depth]) # 자기 자신을 포함 하지 않는 경우 

bt(0, 0)
print(ans)