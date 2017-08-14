def quickSort(L, low, high):
    i = low
    j = high
    if(i >= j):
        return L
    key = L[i]
    while(i < j):
        #从右向左寻找是否有比Key小的数
        while i < j and L[j] >= key:
            j = j - 1
        L[i] = L[j]
        #从左向右寻找是否有比Key大的数
        while i < j and L[i] <= key:
            i = i + 1 
        L[j] = L[i]
    L[i] = key
    quickSort(L, low, i-1)
    quickSort(L, i+1, high)
    return L