def binarysearch(list, gesucht):
    low = 0
    high = len(list) - 1
    gefunden = False
    while low < high and not gefunden:
        mid = (low+high) // 2
        midValue = list[mid]
        if midValue == gesucht:
            gefunden = True
            print('Deine Zahl ist vorhanden.')
        elif midValue < gesucht:
            low = mid + 1
        else:
            high = mid
    if not gefunden:
        print('Zahl nicht da.')

def linearsearch(list, gesucht):
    gefunden = False
    for i in range(0, len(list)):
        if list[i] == gesucht:
            print('Deine Zahl ist vorhanden.')
            gefunden = True
    if not gefunden:
        print('Zahl nicht da.')

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
gesuchtezahl = False
while not gesuchtezahl:
    try:
        gesuchtezahl = int(input('Zu suchende Zahl: '))
    except ValueError:
        print('Bitte nur ganze Zahlen!')

auswahl = False
while not auswahl:
    try:
        auswahl = int(input('''
Linearsearch: 1
Binarysearch: 2
'''))
    except ValueError:
        print('Bitte nur Zahlen!')
print('')

if not auswahl - 1:
    linearsearch(list, gesuchtezahl)
    print('linear')
else:
    binarysearch(list, gesuchtezahl)
    print('binary')
    
#match auswahl:
#    case 1:
#        linearsearch(list, gesuchtezahl)
#    case 2:
#        binarysearch(list, gesuchtezahl)
#    case _: 
#        print('Zahl (1-2)!!!!!!!')