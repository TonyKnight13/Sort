def insertionSort(L):
    n = len(L)
    for i in range(1, n):
        k = L[i]
        j = i - 1
        while(j >= 0):
            if(L[j] > k):
                L[j + 1] = L[j]
                L[j] =  k
            j -= 1
    return L 