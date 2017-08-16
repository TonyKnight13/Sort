'''
 思路：
 
'''
#正序
def bubbleSort(L):
    n = len(L)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if(L[j] > L[j + 1]):
               L[j + 1], L[j] = L[j], L[j + 1] 
    return L

#倒序
def bubbleSortV2(L):
    n = len(L)
    for i in range((n - 1), 0, -1):
        for j  in range(i):
            if(L[j] > L[j + 1]):
               L[j + 1], L[j] = L[j], L[j + 1] 
    return L       