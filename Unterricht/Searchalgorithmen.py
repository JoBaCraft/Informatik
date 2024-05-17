def binarysearch(list, gesucht):
    low = 0
    high = len(list) - 1
    gefunden = False

    while low < high:
        mid = (low+high) // 2
        midValue = list[mid]
        if midValue == gesucht:
            gefunden = True
            print('deine Zahl ist vorhanden')
            break
        elif midValue < gesucht:
            low = mid + 1
        else:
            high = mid
    
    if not gefunden:
        print('Zahl nicht da')


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
gesuchtezahl = int(input('Zu suchende Zahl: '))
binarysearch(list, gesuchtezahl)