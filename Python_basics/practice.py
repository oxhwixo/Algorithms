# print("Quiz 1--------------------------")
# station = "사당"
# print(station + "행 열차가 들어오고 있습니다.")
# station = "신도림"
# print(station + "행 열차가 들어오고 있습니다.")
# station = "인천공항"
# print(station + "행 열차가 들어오고 있습니다.")

# print("Quiz 2--------------------------")
# from random import *
# day = randint(4,28)
# print("오프라인 스터디 모임 날짜는 매월 " + str(day) + " 일로 선정되었습니다.")

# print("Quiz 3--------------------------")
# site = "http://naver.com"
# domain_name = site[7:site.index(".")]
# # domain_name = site.replace("http://", "") 로도 가능!! 
# secreat = domain_name[:3] + str(len(domain_name)) + str(domain_name.count("e")) + "!"
# print("생성된 비밀번호 : %s" % secreat)

# print("Quiz 4--------------------------")
# id = list(range(1,21))
# winner = sample(id, 1)
# id.remove(winner[0])
# print("--- 당첨자 발표 ---")
# print("치킨 당첨자: %d" % winner[0])
# winner = sample(id, 3)
# print("커피 당첨자 : ", end="")
# print(winner)

# print("Quiz 5--------------------------")
# customer = list(range(5))
# i = 0
# count = 0
# while i < 5 :
# 	customer[i] = randint(5,50)
# 	check = " "
# 	if 5 < customer[i] < 15 :
# 		check = "O"
# 		count += 1
# 	print("[{0}] {1}번째 손님 (소요시간: {2}분)".format(check,i+1,customer[i]))
# 	i += 1
# print("총 탑승 승객 : {0} 분".format(count))

# print("Quiz 6--------------------------")
# def std_weight(height, gender):
# 	if gender == "남":
# 		weight = height**2 * 22 
# 	elif gender == "여":
# 		weight = height**2 * 21
# 	return weight
	
# height = float(input("키를 입력하시오: "))
# gender = input("성별을 입력하시오 (남 or 여): ")
# weight = round(std_weight(height / 100, gender), 2)
# print("키 {0}cm {1}자의 표준 체중은 {2}kg 입니다."\
# 	.format(height,gender,weight))

# print("Quiz 7--------------------------")
# class SoldOutError(Exception):
# 	pass

# chicken = 10
# waiting = 1
# while(True):
# 	try:
# 		print("[남은 치킨 : {0}]".format(chicken))
# 		order = int(input("치킨을 몇 마리 주문하시겠습니까?"))
# 		if order < 1:
# 			raise ValueError
# 		elif order > chicken:
# 			 print("재료가 부족합니다.")
# 		else:
# 			print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다.".format(waiting, order))
# 			waiting += 1
# 			chicken -= order

# 		if chicken == 0:
# 			raise SoldOutError
		
# 	except ValueError:
# 		print("잘못된 값을 입력하였습니다.")

# 	except SoldOutError:
# 		print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
# 		break
