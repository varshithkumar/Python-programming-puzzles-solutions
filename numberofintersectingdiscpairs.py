def solution(A):
    # write your code in Python 2.7
    upper = sorted([(i+val) for i, val in enumerate(A)])
    lower = sorted([(i-val) for i, val in enumerate(A)])
    
    j=0
    counter = 0
    
    for i, uval in enumerate(upper):
        while j<len(upper) and uval >= lower[j]:
            counter += j-i
            j+=1
        if counter > 10**7:
            return -1
    return counter  