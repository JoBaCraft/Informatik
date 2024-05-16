def swap(list,i,j):
    list[i], list[j] = list[j], list[i]
    
def selectionsort(list):
    size = len(list)
    for i in range(size):
        min_index = 1
        for j in range(i + 1, size):
            if list[j] < list[min_index]:
                min_index = j
        list[i], list[min_index] = list[min_index], list[i]
    print(list)
    
def insertionsort(list):
    size = len(list)
    if size <= 1:
        return
    for i in range(1, size):
        key = list[i]
        j = i-1
        while j>= 0 and key < list[j]:
            list[j+1] = list[j]
            j-= 1
        list[j+1] = key
    print(list)
    
def bubblesort(list):
    sortiert = False
    while not sortiert:
        sortiert = True
        i = 0
        while i < len(list)-1:
            if list[i] > list[i+1]:
                swap(list,i,i+1)
                sortiert = False
            i += 1
    print(list)
    
list = []
listsize = int(input('Laenge der Liste: '))

while len(list) < listsize:
    Zahl = int(input('Zahl fuer die Liste: '))
    list.append(Zahl)

auswahl = int(input('''
Selectionsort: 1
Insertionsort: 2
Bubblesort: 3


                        '''))
    
match auswahl:
    case 1:
        selectionsort(list)
    
    case 2:
        insertionsort(list)
        
    case 3:
        bubblesort(list)
        
        
        