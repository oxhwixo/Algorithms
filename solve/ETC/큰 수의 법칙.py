N, M, K = map(int, input().split())
array = list(map(int, input().split()))

array.sort()
max_num = array[N - 1]
next_max_num = array[N - 2]

count = (int(M / (K + 1)) * K) + (M % (K + 1))
result = count * max_num
result += (M - count) * next_max_num

print(result)