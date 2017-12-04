def solution(A):
    # write your code in Python 2.7
    C = [0] * (max(A) + 1)
    for i in range(max(A)):
        if i > 0:
            if i in A:
                C[i] += 1
                
    for i in range(1,len(C)):
        if C[i] == 0:
            return i
            