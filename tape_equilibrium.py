
def solution(A):
    head = A[0]
    tail = sum(A[1:])
    min_dif = abs(head - tail)
 
    for index in range(1, len(A)-1):
        head += A[index]
        tail -= A[index]
        if abs(head-tail) < min_dif:
            min_dif = abs(head-tail)
 
    return min_dif

def solution(A):
    # write your code in Python 2.7
    if len(A) == 2:
        return abs(A[0] - A[1])
    minimum = abs(A[0] - sum(A[1:]))
    for i in range(2,len(A) - 1):
        temp = abs(sum(A[:i]) - sum(A[i:]))
        if temp < minimum:
            minimum = temp
    return minimum  