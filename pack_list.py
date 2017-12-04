def pack_list(arr):
	result = []
	count = 0
	for i in range(len(arr)):
		
		if i == (len(arr)-1):
			if arr[i] == arr[i-1]:
				result[len(result)-1].append(arr[i])
			else:
				result.append([arr[i]])
		elif arr[i] == arr[i+1]:		
			count += 1
		else:
			result.append(arr[(i-count):i+1])
			count = 0
	return result

print(pack_list([1,1,1,1,2,2,4,4,4,4,4,5,6,7,7,8,8,9]))


			