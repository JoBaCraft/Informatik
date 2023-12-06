einkaufszettel = [[1, 'milch', 2.0], [2, 'eier', 3.0]]                # zum einfachen testen
#einkaufszettel = []
element = []

antwort = input('Moechtest du eine Einkaufsliste anlegen? (ja/nein):  ')
while antwort == "ja": 
    print('')
    operation = int(input('1 = hinzufuegen, 2 = entfernen, 3 = Anzahl erhoehen, 4 = pruefen, 5 = Preis berechnen:  '))
    match operation:

        case 1:
            artikel = input('Was moechtest du hinzufuegen?:  ')
            anzahl = int(input('Wie oft?: '))
            preis = float(input('Wie teuer?: '))
            element = [anzahl, artikel, preis]
            if element[1] in sum(einkaufszettel, []):
                print('Ist schon drin')
                print('')
                add = input('Moechtest du etwas hinzufuegen? (ja/nein): ')
                if add == "ja":
                    anzahl = int(input('Wie viel moechtest du hinzufuegen?:  '))
                    for i, element in enumerate(einkaufszettel):
                        if element[1] == artikel:
                            einkaufszettel[i][0] += anzahl
            else:
                einkaufszettel.append(element)

        case 2:
            artikel = input('Was moechtest du entfernen?:  ')
            anzahl = int(input('Wie viel moechtest du entfernen?:  '))
            for i, element in enumerate(einkaufszettel): 
                if element[1] == artikel:
                    einkaufszettel[i][0] -= anzahl
                    if einkaufszettel[i][0] <= 0:
                        del einkaufszettel[i]
                else:
                    print('Der Artikel ist nicht in der Liste.')

        case 3:
            artikel = input('Wovon moechtest du mehr?:  ')
            anzahl = int(input('Wie viel moechtest du hinzufuegen?:  '))
            for i, element in enumerate(einkaufszettel):
                if element[1] == artikel:
                    einkaufszettel[i][0] += anzahl
                else:
                    print('Der Artikel ist noch nicht in der Liste. ')

        case 4:
            artikel = input('Was willst du pruefen?:  ')  
            if artikel in sum(einkaufszettel, []):
                print('Ist schon drin.')   
            else:
                print('Ist noch nicht drin.')
        
        case 5:
            gesamtpreis = 0
            for i, element in enumerate(einkaufszettel):
                gesamtpreis += element[0] * element[2]
            print('Dein Einkaufszettel kostet', f'{gesamtpreis: .2f}', 'Euro.')
        
    print('')            
    print(einkaufszettel)
    print('')
    antwort = input('willst du noch mehr aendern? (ja/nein):  ')

print('Dein Einkaufszettel ist:', einkaufszettel)