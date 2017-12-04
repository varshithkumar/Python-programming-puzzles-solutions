def solution(A):
    passing = 0
    west = 0
    for i in range(len(A)-1, -1, -1):
        if A[i] == 0:
            passing+=west
            if passing > 1000000000:
                return -1
        else:
            west+=1
    return passing