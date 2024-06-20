def merge(array, low, mid, high):
    subArray1 = mid - low + 1
    subArray2 = high - mid
    
    leftArray = [0] * subArray1
    rightArray = [0] * subArray2
    
    for i in range(subArray1):
        leftArray[i] = array[low + i]
    for j in range(subArray2):
        rightArray[j] = array[mid + 1 + j]
        
    IndexSubArray1 = IndexSubArray2 = 0
    IndexMergedArray = low
    
    while IndexSubArray1 < subArray1 and IndexSubArray2 < subArray2:
        if leftArray[IndexSubArray1] <= rightArray[IndexSubArray2]:
            array[IndexMergedArray] = leftArray[IndexSubArray1]
            IndexSubArray1 += 1
        else:
            array[IndexMergedArray] = rightArray[IndexSubArray2]
            IndexSubArray2 += 1
        IndexMergedArray += 1
    
    while IndexSubArray1 < subArray1:
        array[IndexMergedArray] = leftArray[IndexSubArray1]
        IndexSubArray1 += 1
        IndexMergedArray += 1
        
    while IndexSubArray2 < subArray2:
        array[IndexMergedArray] = rightArray[IndexSubArray2]
        IndexSubArray2 += 1
        IndexMergedArray += 1


def mergesort(array, low, high):
    if low >= high:
        return
    mid = low + (high - low) // 2
    mergesort(array, low, mid)
    mergesort(array, mid+1, high)
    merge(array, low, mid, high)


liste = [54,65,24,2,9]
print(mergesort(liste, 0, len(liste)-1))