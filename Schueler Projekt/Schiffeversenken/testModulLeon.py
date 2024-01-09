def zeigeSpielersicht(feld):
    i = 0
    print ('  1 2 3 4 5 6 7 8')
    while i < 8:
        j = 0
        zeilentext = str(i+1) + ' '
        while j < 8:
            if feld[i][j] == 'S' or feld[i][j] == 'A': #Schiffe/Abstandsfelder nicht zeigen
                zeilentext = zeilentext + '~ '
            else:
                zeilentext = zeilentext + feld[i][j] + ' '
            j = j + 1
        i = i + 1
        print(zeilentext)    
    print('') #Leerzeile nach dem Feld
    
def zeigeComputersicht(feld):
    i = 0
    print ('  1 2 3 4 5 6 7 8')
    while i < 8:
        j = 0
        zeilentext = str(i+1) + ' '
        while j < 8:
            if feld[i][j] == 'A':
                zeilentext = zeilentext + '~ '
            else:
                zeilentext = zeilentext + feld[i][j] + ' '
            j = j + 1
        i = i + 1
        print(zeilentext)    
    print('') #Leerzeile nach dem Feld 