'''
   思路：

'''

def merge(left, right):
    r, l = 0, 0
    result = []
    while(l < len(left) and r < len(right)):
        if(left[l] < right[r]):
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]
    return result

def mergeSort(L):
    if len(L) <= 1:
        return L
    n = int(len(L) / 2)
    l =  mergeSort(L[:n])
    r =  mergeSort(L[n:])
    return merge(l, r)