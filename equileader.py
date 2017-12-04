def solution(A):
    # write your code in Python 2.7
    d = {}
    leader = None
    array = []
    count = 0
    lcount = 0
    for i in A:
        d[i] = 0
    for i in A:
        d[i] += 1
    for i in d:
        if d[i]>(len(A))//2:
            leader = i
            count = d[i]
    
    for i in range(len(A)-1):
        if A[i] == leader:
            lcount+=1
            count-=1
        if lcount>((i+1)//2) and count>(len(A)-(i+1))//2:
            array.append(i)
    
    return len(array) 