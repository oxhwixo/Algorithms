import math

math.ceil(3.5) # 올림
math.floor(3.5) # 내림
round(3.5) # 반올림

# round는 사사오입 원칙을 따르기에 반올림 할 자리의 수가 5일 때
# 앞 수가 짝수면 내림하고 홀수면 올림한다.
# 이에 상관없이 반올림 할 자리의 수가 5일 때
# 무조건 반올림 하려면 직접 제작해야한다.