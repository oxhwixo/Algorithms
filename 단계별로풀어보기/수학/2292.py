n = int(input())
honeycomb = 1
layer = 1

while n > honeycomb :
	honeycomb += 6 * layer
	layer += 1

print (layer)