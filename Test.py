
L = []

def flatten(arr):
	for item in arr:
		if type(item) == list:
			flatten(item)
		else:
			L.append(item)
	return L




