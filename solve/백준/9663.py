# 9663 N-Queen
# 골드 4

import sys
input = sys.stdin.readline

n = int(input())
ans = 0
row = [0] * n # row[행번호] = 열번호 (행, 열)

def is_possible(x): 
    for i in range(x): # i == 행번호, row[i] == 열번호
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    return True

def bt(x): # x == row
    global ans

    if x == n:
        ans += 1
    
    else:
        for i in range(n):
            row[x] = i # (x, i)에 놓기
            if is_possible(x):
                bt(x + 1)

bt(0)
print(ans)