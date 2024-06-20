def printArray(array, size) -> None:
    for i in range(size):
        print(array[i], end=" ")
    print()

def selectionsort(list) -> list[int]:
    size = len(list)
    if size < 2:
        return list     # Basisfall -> Liste <2 Elemente
    for i in range(size):
        min_index = i   # Kleinstes Element default an Stelle i
        for j in range(i + 1, size):    # Element j < Element i ?
            if list[j] < list[min_index]:   
                min_index = j
        list[i], list[min_index] = list[min_index], list[i]    # Switch Elemente
    return list
    
def insertsort(list) -> list[int]:
    size = len(list)
    if size < 2:    # Basisfall -> Liste <2 Elemente
        return list
    for i in range(1, size):
        key = list[i]
        j = i-1
        while j >= 0 and key < list[j]:  
            list[j+1] = list[j]
            j -= 1
        list[j+1] = key
    return list
    
def bubblesort(list) -> list[int]:
    if len(list) < 2:   #basisfall -> Liste <2 Elemente
        return list
    sortiert = False
    while not sortiert:
        sortiert = True
        i = 0
        # Element i wird nach hinten verschoben bis Element j > Element i
        while i < len(list)-1:
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                sortiert = False
            i += 1
    return list

def quicksort(list) -> list[int]:
    if len(list) < 2:   # Basisfall -> Liste <2 Elemente
        return list  
    else:
        pivot = list[0]
        # Divide Elements into lists <pivot OR >=pivot
        left = [x for x in list[1:] if x < pivot]
        right = [x for x in list[1:] if x >= pivot]
        return quicksort(left) + [pivot] + quicksort(right)

def mergeInPlace(list1, list2) -> list[int]:
    list = []
    i = j = 0
    # Insert Elements smallest first
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:     
            list.append(list1[i])
            i += 1
        else:
            list.append(list2[j])
            j += 1
    # Insert remaining Elements 
    while i < len(list1):
        list.append(list1[i])
        i += 1
    while j < len(list2):
        list.append(list2[j])
        j += 1
    return list

def mergesortInPlace(list, low, high) -> list[int]:
    if low >= high:     # Basisfall -> Liste <2 Elemente
        out = [list[low]]
        return out
    mid = (low + high) // 2
    return mergeInPlace(mergesortInPlace(list, low, mid), mergesortInPlace(list, mid+1, high))

def merge(array, low, mid, high) -> None:
    subArray1 = mid - low + 1
    subArray2 = high - mid
    # Create 2 temp arrays
    leftArray = [0] * subArray1
    rightArray = [0] * subArray2
    # Copy Data to temp arrays
    for i in range(subArray1):
        leftArray[i] = array[low + i]
    for j in range(subArray2):
        rightArray[j] = array[mid + 1 + j]
        
    IndexSubArray1 = IndexSubArray2 = 0
    IndexMergedArray = low
    # Merge temp arrays back into array
    while IndexSubArray1 < subArray1 and IndexSubArray2 < subArray2:
        if leftArray[IndexSubArray1] <= rightArray[IndexSubArray2]:
            array[IndexMergedArray] = leftArray[IndexSubArray1]
            IndexSubArray1 += 1
        else:
            array[IndexMergedArray] = rightArray[IndexSubArray2]
            IndexSubArray2 += 1
        IndexMergedArray += 1
    # Copy remaining Elements from left temp array
    while IndexSubArray1 < subArray1:
        array[IndexMergedArray] = leftArray[IndexSubArray1]
        IndexSubArray1 += 1
        IndexMergedArray += 1
    # Copy remaining Elements from right array
    while IndexSubArray2 < subArray2:
        array[IndexMergedArray] = rightArray[IndexSubArray2]
        IndexSubArray2 += 1
        IndexMergedArray += 1

def mergesort(array, low, high) -> None:
    if low >= high: # Basisfall -> Liste <2 Elemente
        return
    mid = low + (high - low) // 2
    mergesort(array, low, mid)
    mergesort(array, mid+1, high)
    merge(array, low, mid, high)

list = []
listsize = False
while not listsize:
    try:
        listsize = int(input('Laenge der Liste: '))
    except ValueError:
        print('Bitte nur ganze Zahlen!')

while len(list) < listsize:
    Zahl = False
    while not Zahl:
        try:
            Zahl = float(input('Zahl fuer die Liste: '))
        except ValueError:
            print('Bitte nur Zahlen!')
    list.append(Zahl)

auswahl = False
while not auswahl:
    try:
        auswahl = int(input('''
Selectionsort: 1
Insertsort: 2
Bubblesort: 3
Quicksort: 4
Mergesort(InPlace): 5
Mergesort(OutOfPlace): 6
'''))
    except ValueError:
        print('Bitte nur Zahlen!')

#python version 3.10+
match auswahl:
    case 1:
        selectionsort(list)
        print('\nSorted List: ')
        printArray(list, len(list))
    case 2:
        insertsort(list)
        print('\nSorted List: ')
        printArray(list, len(list))
    case 3:
        bubblesort(list)
        print('\nSorted List: ')
        printArray(list, len(list))
    case 4:
        quicksort(list)
        print('\nSorted List: ')
        printArray(list, len(list))
    case 5:
        mergesortInPlace(list, 0, len(list)-1)
        print('\nSorted List: ')
        printArray(list, len(list))
    case 6:
        mergesort(list, 0, len(list)-1)
        print('\nSorted List: ')
        printArray(list, len(list))
    case _:
        print('\nZahl von 1 bis 6!')

#python version 3.9-
#if auswahl == 1:
#    selectionsort(list)
#    print('\nSorted List: ')
#    printArray(list, len(list))
#elif auswahl == 2:
#    insertsort(list)
#    print('\nSorted List: ')
#    printArray(list, len(list))
#elif auswahl == 3:
#    bubblesort(list)
#    print('\nSorted List: ')
#    printArray(list, len(list))
#elif auswahl == 4:
#    quicksort(list)
#    print('\nSorted List: ')
#    printArray(list, len(list))
#elif auswahl == 5:
#    mergesortInPlace(list, 0, len(list)-1)
#    print('\nSorted List: ')
#    printArray(list, len(list))
#elif auswahl == 6:
#    mergesort(list, 0, len(list)-1)
#    print('\nSorted List: ')
#    printArray(list, len(list))
#else:
#    print('\nZahl von 1 bis 6!')