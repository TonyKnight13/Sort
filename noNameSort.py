def SortV1(L):
    n = len(L)
    for i in range(n):
        for j in range(i+1, n):
            if(L[j] < L[i]):
                L[i], L[j] = L[j], L[i]
    return L
