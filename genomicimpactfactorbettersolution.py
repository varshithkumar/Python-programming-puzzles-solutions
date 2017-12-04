def solution(S, P, Q):
    # write your code in Python 2.7
    n = len(S)
    A = [0] * n
    C = [0] * n
    G = [0] * n
    T = [0] * n
    for i in range(n):
        if S[i] == 'A':
            A[i] += 1
        elif S[i] == 'C':
            C[i] += 1
        elif S[i] == 'G':
            G[i] += 1
        else:
            T[i] += 1
    
    P_A = prefix(A)
    P_C = prefix(C)
    P_G = prefix(G)
    P_T = prefix(T)
    result = []
    for i, j in zip(P,Q):
        if P_A[j+1] - P_A[i] > 0:
            result.append(1)
        elif P_C[j+1] - P_C[i] > 0:
            result.append(2)
        elif P_G[j+1] - P_G[i] > 0:
            result.append(3)
        else:
            result.append(4)       
    
    return result        

def prefix(l):
    m = len(l)
    P = [0]*(m+1)
    for i in range(1,m+1):
        P[i] = P[i-1] + l[i-1]
    return P