n, newScore, p = map(int, input().split())
if n != 0:
	scores = list(map(int, input().split()))
else:
	scores = []

scores.append(newScore)
scores.sort(reverse=True)

def func():
    index = 0

    if n == p:
        if scores[-1] < newScore:
            scores.append(newScore)
        else:
            return -1

    for i in range(n):
        if newScore == scores[i]:
            index = i

    while True:
        if index == 0:
            break
        else:
            if scores[index] == scores[index-1]:
                index -= 1
                continue
            else:
                break

    return index + 1

result=func()
print(result)
