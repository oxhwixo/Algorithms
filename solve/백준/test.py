n = int(input())
arr = list(map(int, input().split()))

if n == 1:
    print(sum(arr[:5]))
    exit(0)

temp = []

temp.append(min(arr[0], arr[5]))
temp.append(min(arr[1], arr[4]))
temp.append(min(arr[2], arr[3]))
temp.sort()

fir = temp[0]
sec = temp[0] + temp[1]
thi = sum(temp)

result = thi * 4 + sec * (4 * (n - 1) + 4 * (n - 2)) + fir * (4 * (n - 2) * (n - 1) + (n - 2) ** 2)

print(result)