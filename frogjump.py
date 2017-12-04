def solution(X, Y, D):
    # write your code in Python 2.7
    if (Y-X)%D == 0:
        return (Y-X)/D
    else:
        return ((Y-X)//D)+1