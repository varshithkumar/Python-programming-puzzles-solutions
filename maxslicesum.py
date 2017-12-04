def solution(A):
    currentsum = maxsum = A[0]
    
 
    for element in A[1:]:
        currentsum = max(element, currentsum+element)
        maxsum = max(maxsum, currentsum)
 
    return maxsum