def solution(A, B, K):
    # write your code in Python 2.7
    if A%K != 0:
        return ((B-(K-(A%K)+A))//K) + 1
    elif A%K == 0:
        return ((B-A)//K) + 1