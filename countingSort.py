'''
   思路：

'''

def countingSort(L):
    n = len(L)
    b = [0] * n
    c = [0] * n
    for i in range(n):
        for j in range(i+1, n):
            if(L[i] > L[j]):
                b[i] += 1
            else:
                b[j] += 1
    for i in range(n):
        c[b[i]] = L[i]
    return c