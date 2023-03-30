import sys
input = sys.stdin.readline

n = int(input())
row = [0] * n
cnt = 0

def is_possible(depth): 
    for i in range(depth):
        if row[depth] == row[i] or abs(row[depth] - row[i]) == abs(depth - i):
            return False
    return True

def bt(depth):
    global cnt

    if depth == n:
       cnt += 1
       return 

    else:
       for i in range(n):
        row[depth] = i
        if is_possible(depth):
          bt(depth + 1)

bt(0)
print(cnt)