def solution(X, A):
    # write your code in Python 2.7
    time = 0
    covered = [-1] * (X+1)
    for index,element in enumerate(A):
        if covered[element] == -1:
            covered[element] = element
            time += 1
            if time == X:
                return index
    return -1 