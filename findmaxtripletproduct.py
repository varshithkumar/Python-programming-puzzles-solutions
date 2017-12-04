def solution(A):
    # write your code in Python 2.7
    n = len(A)
    A.sort()
    return max((A[0]*A[1]*A[n-1]),(A[n-1]*A[n-2]*A[n-3]))