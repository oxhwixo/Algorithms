# 10진수를 2진수로 만들고 포화이진트리를 만든다!라고 생각하면 안됨
# 이진트리를 포화이진트리로 만들어서 2진수로 표현하는 방법이 우선 먼저!!
# 그 방법으로 10->2진수 변환이 되는지를 찾는것
# 유효한 노드는 1이 들어가며 더미 노드는 0이 들어감
# 유효한 노드에 더미 노드를 채워서 2진수를 만들 수 있음

import math

def check(binary, prev_parent): #prev_parent는 부모가 1일때 True 0일때 False
    mid = len(binary) // 2
    if binary:
        son = binary[mid] =='1'
    else: return True

    if son and not prev_parent: # 현재 노드가 1인데 부모가 0이었으면 Return False
        return False
    else:
        return check(binary[mid + 1:], son) and check(binary[:mid], son)

def sol(num):
    if num == 1: return 1
    
    binary = bin(num)[2:]
    digit = 2 ** (int(math.log2(len(binary))) + 1) - 1
    binary = "0" * (digit - len(binary)) + binary
    
    if binary[len(binary) // 2] == '1' and check(binary, True): return 1
    else: return 0

def solution(numbers):
    answer = []
    for num in numbers:
        answer.append(sol(num))
    return answer