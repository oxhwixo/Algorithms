print("Quiz 1--------------------------")
station = "사당"
print(station + "행 열차가 들어오고 있습니다.")
station = "신도림"
print(station + "행 열차가 들어오고 있습니다.")
station = "인천공항"
print(station + "행 열차가 들어오고 있습니다.")

print("Quiz 2--------------------------")
from random import *
day = randint(4,28)
print("오프라인 스터디 모임 날짜는 매월 " + str(day) + " 일로 선정되었습니다.")

print("Quiz 3--------------------------")
site = "http://naver.com"
domain_name = site[7:site.index(".")]
# domain_name = site.replace("http://", "") 로도 가능!! 
secreat = domain_name[:3] + str(len(domain_name)) + str(domain_name.count("e")) + "!"
print("생성된 비밀번호 : %s" % secreat)

print("Quiz 4--------------------------")
id = list(range(1,21))
winner = sample(id, 1)
id.remove(winner[0])
print("--- 당첨자 발표 ---")
print("치킨 당첨자: %d" % winner[0])
winner = sample(id, 3)
print("커피 당첨자 : ", end="")
print(winner)