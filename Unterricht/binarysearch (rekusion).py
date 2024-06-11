def binarysearch(low, high, gesuchteZahl, list):
    mid = (low + high) // 2
    
    if low > high:
        return -1
    
    if list[mid] == gesuchteZahl:
        return mid
    
    if low == high:
        if list[mid] == gesuchteZahl:
            return mid
        else:
            return -1
        
    if list[mid] > gesuchteZahl:
        return binarysearch(mid + 1, len(list) - 1, gesuchteZahl, list)
    
    if list[mid] < gesuchteZahl:
        return binarysearch(0, mid - 1, gesuchteZahl, list)
    
    
list = [1, 2, 3, 4, 6, 7, 8, 9, 10]
print(binarysearch(0, len(list) - 1, 5, list))