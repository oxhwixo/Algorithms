a = list(input())

for i in range(len(a)):
	if a[i].isupper():
		a[i] = a[i].lower()
	else:
		a[i] = a[i].upper()
print(''.join(s for s in a))