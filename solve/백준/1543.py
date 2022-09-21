# 1543 문서 검색
# 실버 4

data = input()
word = input()

word_len = len(word)
count  = 0
i = 0

while i < len(data):
	if data[i : i+word_len] == word:
		count += 1
		i += word_len
	else:
		i += 1

print(count)

# aabb - ab 인 경우 틀림
# for i in range(0,len(data), word_len) 
# word_len 크기만큼 건너뛰었는데 그럴 필요가 없었음
# for문이 아니라 while을 사용해보자