# 2744 대소문자 바꾸기 
# 브론즈 5

a = list(input())

for i in range(len(a)):
	if a[i].isupper(): # 대소문자 확인 방법
		a[i] = a[i].lower() # 대소문자 변환 
	else:
		a[i] = a[i].upper()
print(''.join(s for s in a)) # 리스트를 문자열로 변환하는 방법