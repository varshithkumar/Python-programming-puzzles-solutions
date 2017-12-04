
L = []

def flatten(arr):
	for item in arr:
		if type(item) == list:
			flatten(item)
		else:
			L.append(item)
	return L

print (flatten([1,2,[3,4,[5,6],5],[4,5,6],8,9]))


