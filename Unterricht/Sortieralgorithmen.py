def swap(list,i,j):
    list[i], list[j] = list[j], list[i]
    
def selectionsort(list):
    size = len(list)
    for i in range(size):
        min_index = i
        for j in range(i + 1, size):
            if list[j] < list[min_index]:
                min_index = j
        list[i], list[min_index] = list[min_index], list[i]
    print(f'''
Genutzter Algorithmus: Selectionsort
Sortierte Liste: {list}
''')
    
def insertsort(list):
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
    print(f'''
Genutzter Algorithmus: Insertsort
Sortierte Liste: {list}
''')
    
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
    print(f'''
Genutzter Algorithmus: Bubblesort
Sortierte Liste: {list}
''')
    
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
'''))
    except ValueError:
        print('Bitte nur Zahlen!')
print('')
    
match auswahl:
    case 1:
        selectionsort(list)
    case 2:
        insertsort(list)
    case 3:
        bubblesort(list)
    case _:
        print('Zahl (1-3)!!!!!!')

#if auswahl == 1:
#    selectionsort(list)
#elif auswahl == 2:
#    insertsort(list)
#elif auswahl == 3:
#    bubblesort(list)  
#else:
#    print('Zahl (1-3)!!!!!!')