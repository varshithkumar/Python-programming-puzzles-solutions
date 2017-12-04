def solution(A):
    # write your code in Python 2.7
    c = [0] * (len(A)+2)
    for num in A:
        if num>0 and num<=len(A)+1:
            c[num]+=1
            
    for i in range(1, len(A)+2):
        if c[i] == 0:
            return i
    
    raise Exception('Should never be here')
    return -1