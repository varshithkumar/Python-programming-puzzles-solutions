def solution(A):
    # write your code in Python 2.7
    leader = None
    d = {}
    for i in A:
        d[i] = 0
    for i in A:
        d[i]+=1
    for k in d:
        if d[k] > len(A)//2:
            leader = k
    if leader == None:
        return -1
    else:
        return A.index(leader)
        