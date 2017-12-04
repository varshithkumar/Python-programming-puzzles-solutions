def solution(S, P, Q):
    # write your code in Python 2.7
    A = []
    for i,j in zip(P,Q):
        if 'A' in S[i:(j+1)]:
            A.append(1)
        elif 'C' in S[i:(j+1)]:
            A.append(2)
        elif 'G' in S[i:(j+1)]:
            A.append(3)
        elif 'T' in S[i:(j+1)]:
            A.append(4)
    return A  