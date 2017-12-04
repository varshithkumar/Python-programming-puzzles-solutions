def maxcont_sum(arr):

  max_sum = current_sum = arr[0]

  for num in arr[1:]:

    current_sum = max(current_sum+num, num)

    max_sum = max(current_sum, max_sum)

  return max_sum
  


print (maxcont_sum([1,2,-2,3,-56,99,123,3,4,5,6,-90]))  