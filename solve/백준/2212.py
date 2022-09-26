# 2212 센서
# 골드 5

# N개의 센서 - K개의 집중국을 세움. 
# N개의 센서가 적어도 하나의 집중국과 통신 가능
# 각 집중국의 수신 가능 영역의 길이 합을 최소화 

n = int(input()) # 센서의 개수
k = int(input()) # 집중국의 개수
sensors = list(map(int, input().split()))

sensors.sort()
sensors_distance = [sensors[i] - sensors[i-1] for i in range(1, n)]
sensors_distance.sort()

print(sum(sensors_distance[:n - k]))

