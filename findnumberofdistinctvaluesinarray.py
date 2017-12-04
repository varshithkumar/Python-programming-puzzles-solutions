def solution(A):
    # write your code in Python 2.7
    if len(A)==0:
        return 0
    result = 1
    n = len(A)
    A.sort()
    for i in xrange(1, n):
        if A[i]!=A[i-1]:
            result+=1
    return result