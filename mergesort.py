def mergesort(arr):
	if len(arr)<2:
		return arr
	mid = len(arr)//2
	left = mergesort(arr[:mid])
	right = mergesort(arr[mid:])
	
	i, j = 0, 0
	result = []
	
	while i<len(left) and j<len(right):
		if left[i] < right[j]:
			result.append(left[i])
			i+=1
		else:
			result.append(right[j])
			j+=1
	if left[i:]:
		result.extend(left[i:])
	if right[j:]:
		result.extend(right[j:])

	return result

print(mergesort([2,3,1,5,9,5,6,7,3,2,1,0]))