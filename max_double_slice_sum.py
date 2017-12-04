def solution(A):
    # write your code in Python 2.7
    n = len(A)
    max_beginning_here = [0]*n
    max_beginning_here_temp = 0
    for i in range(1,n-2):
        max_beginning_here_temp = max(0,max_beginning_here_temp+A[i])
        max_beginning_here[i] = max_beginning_here_temp
        
    max_ending_here = [0]*n
    max_ending_here_temp = 0
    for i in range(n-2,1,-1):
        max_ending_here_temp = max(0,max_ending_here_temp+A[i])
        max_ending_here[i] = max_ending_here_temp
        
    max_slice_sum = 0
    for i in range(0,n-2):
        max_slice_sum = max(max_slice_sum, max_beginning_here[i] + max_ending_here[i+2])
        
    return max_slice_sum 