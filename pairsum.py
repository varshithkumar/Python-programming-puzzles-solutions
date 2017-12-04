def pairsum(arr,k):
  
  
	if len(arr) < 2:
    
		return 'not a valid input'
  
	output = set()
  
	seen = set()
  
  
	for num in arr:
		target = k - num
		if target not in seen:

                	seen.add(num)
    
		else:

      			output.add((min(num, target), max(num,target)))

      
  return  len(output)


print (pairsum([1,2,3,2], 4))  