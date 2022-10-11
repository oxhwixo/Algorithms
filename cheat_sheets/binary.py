def binary_search (array, target, start, end):
	while start <= end:
		mid = (start + end) // 2
		if array[mid] == target:
			return mid
		elif array[mid] > target:
			end = mid - 1
		else:
			start = mid + 1

	return None 

n = int(input())
supply = list(map(int, input().split()))
supply.sort()

m = int(input())
demand = list(map(int, input().split()))

for i in demand:
	result = binary_search(supply, i, 0, n - 1)
	if result == None:
		print("no", end = ' ')
	else:
		print("yes", end = ' ')
