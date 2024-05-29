from random import randint

 # Groesse des Feldes
gewuenschteFeldGroesse = int(input("Feldgroesse: "))
FeldGroesse = 0
ZeilenGroesse = 0
zeile = []
feld = []
AnzahlSFelder = 0


#Das Zeug ausm Testmodul
def zeigeSpielersicht(feld):
    i = 0

    AnzahlZahlen = 0
    Zahl = 1
    Zahlen = [" "]

    while  AnzahlZahlen < gewuenschteFeldGroesse:
        Zahlen.append(" ")
        Zahlen.append(Zahl) # type: ignore
        Zahl += 1
        AnzahlZahlen += 1
    print(*Zahlen, sep="") #Schönes Ausgeben der Listen
    

    while i < gewuenschteFeldGroesse:
        j = 0
        zeilentext = str(i+1) + ' '
        while j < gewuenschteFeldGroesse:
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

    AnzahlZahlen = 0
    Zahl = 1
    Zahlen = [" "]

    while  AnzahlZahlen < gewuenschteFeldGroesse:
        Zahlen.append(" ")
        Zahlen.append(Zahl) # type: ignore
        Zahl += 1
        AnzahlZahlen += 1
    print(*Zahlen, sep="") #Schönes Ausgeben der Listen


    while i < gewuenschteFeldGroesse:
        j = 0
        zeilentext = str(i+1) + ' '
        while j < gewuenschteFeldGroesse:
            if feld[i][j] == 'A':
                zeilentext = zeilentext + '~ '
            else:
                zeilentext = zeilentext + feld[i][j] + ' '
            j = j + 1
        i = i + 1
        print(zeilentext)    
    print('') #Leerzeile nach dem Feld 


#Hier ist wieder normales Programm
while FeldGroesse < gewuenschteFeldGroesse:
    zeile = []
    ZeilenGroesse = 0
    while ZeilenGroesse < gewuenschteFeldGroesse: 
        zeile.append("~")
        ZeilenGroesse += 1
    zeile.append(" ")
    feld.append(zeile)
    #zeile = []
    FeldGroesse += 1
feld.append(zeile)


#Ausgabe der Spielfelder
#print(feld) Einzeilige Ausgabe zur Überpruefung
print("Spielersicht:")
zeigeSpielersicht(feld)

print("Computersicht:")
zeigeComputersicht(feld)


#Zufallsverteilung der Schiffchen
def Schiffplatzierung():
    VorhandeneSchiffe = 0
    AnzahlSFelder = 0
    AnzahlSchiffe = int(input("Anzahl der Einer-Schiffchen: "))

    #Hilfsvariablen für DIE FORMEL
    f = float(FeldGroesse/2)
    i = int(f)
    #DIE FORMEL
    while AnzahlSchiffe > f**2:
        print("Das sind zuviele Schiffe, try again :( ")
        print(AnzahlSchiffe)
        AnzahlSchiffe = int(input("Anzahl der Einer-Schiffchen: "))
        
    while AnzahlSchiffe > VorhandeneSchiffe:
        SchiffZeile = randint(0, FeldGroesse-1)
        SchiffSpalte = randint(0, FeldGroesse-1)
        print(SchiffZeile) #Zur Überpruefung bei Errors
        print(SchiffSpalte) #Zur Überpruefung bei Errors
        
    #Die oberste Zeile 
        if SchiffZeile == 0 : 
            feld[SchiffZeile][SchiffSpalte] = "S"

            feld[SchiffZeile+1][SchiffSpalte] = "A"
            feld[SchiffZeile+1][SchiffSpalte+1] = "A"
            feld[SchiffZeile][SchiffSpalte+1] = "A"
            if SchiffSpalte >= 1:
                feld[SchiffZeile][SchiffSpalte-1] = "A"
            AnzahlSFelder += 1
            VorhandeneSchiffe += 1

    #Die unterste Zeile
        if SchiffZeile == 7:
            feld[SchiffZeile][SchiffSpalte] = "S"

            feld[SchiffZeile-1][SchiffSpalte] = "A"
            feld[SchiffZeile-1][SchiffSpalte-1] = "A"
            feld[SchiffZeile][SchiffSpalte-1] = "A"
            feld[SchiffZeile-1][SchiffSpalte+1] = "A"
            AnzahlSFelder += 1
            VorhandeneSchiffe += 1


        if feld[SchiffZeile][SchiffSpalte] != "S":
            if feld[SchiffZeile-1][SchiffSpalte] != "S":
                if feld[SchiffZeile-1][SchiffSpalte-1] != "S":
                    if feld[SchiffZeile][SchiffSpalte-1] != "S": 
                        if feld[SchiffZeile+1][SchiffSpalte-1] != "S": 
                            if feld[SchiffZeile+1][SchiffSpalte] != "S": 
                                if feld[SchiffZeile+1][SchiffSpalte+1] != "S":
                                    if feld[SchiffZeile][SchiffSpalte+1] != "S": 
                                        if feld[SchiffZeile-1][SchiffSpalte+1] != "S": 
                    
                                            #Abstandsfelder
                                            feld[SchiffZeile][SchiffSpalte] = "A"
                                            feld[SchiffZeile-1][SchiffSpalte] = "A"
                                            feld[SchiffZeile-1][SchiffSpalte-1] = "A"
                                            feld[SchiffZeile][SchiffSpalte-1] = "A"
                                            feld[SchiffZeile+1][SchiffSpalte-1] = "A"
                                            feld[SchiffZeile+1][SchiffSpalte] = "A"
                                            feld[SchiffZeile+1][SchiffSpalte+1] = "A"
                                            feld[SchiffZeile][SchiffSpalte+1] = "A"
                                            feld[SchiffZeile-1][SchiffSpalte+1] = "A"

                                            feld[SchiffZeile][SchiffSpalte] = "S"
                                            AnzahlSFelder += 1
                                            VorhandeneSchiffe += 1
    return AnzahlSFelder
Schiffplatzierung()
print("Computersicht:")
zeigeComputersicht(feld)
print(f"Aufgrund der Zufallsverteilung wurden {AnzahlSFelder} geplaced :).")

#Beschuss
getroffenenFelder = 0
GebrauchteSchuesse = 0
while getroffenenFelder < AnzahlSFelder:
    SchussZeile = int(input("Zeile: "))
    print('')

    #whileschleife sorgt dafür, dass man keine zu grosse Zahl eingeben kann und so ein Error verhindert wird
    while SchussZeile > gewuenschteFeldGroesse:
        print(f"Deine eingegebene Zahl ist zu gross. Die Feldgroesse betraegt nur {gewuenschteFeldGroesse} Felder")
        SchussZeile = int(input("Zeile: "))
        print('')
        
    #whileschleife sorgt dafür, dass man keine zu grosse Zahl eingeben kann und so ein Error verhindert wird
    SchussSpalte = int(input("Spalte: "))
    print('')
    while SchussSpalte > gewuenschteFeldGroesse:
        print(f"Deine eingegebene Zahl ist zu gross. Die Feldgroesse betraegt nur {gewuenschteFeldGroesse} Felder")
        SchussSpalte = int(input("Spalte: "))
        print('')

    #Treffer als "T" markieren
    if feld[SchussZeile - 1][SchussSpalte - 1] == "S":
        feld[SchussZeile - 1][SchussSpalte - 1] = "T"
        getroffenenFelder += 1
        GebrauchteSchuesse += 1
        print('Treffer!!')
    
    #Fehlschüsse als solche markieren
    elif feld[SchussZeile - 1][SchussSpalte - 1] == "~" or feld[SchussZeile - 1][SchussSpalte - 1] == "A":
        feld[SchussZeile - 1][SchussSpalte - 1] = "X"
        GebrauchteSchuesse += 1
        print('Leider daneben. Versuch es nocheinmal.')
    
    print("Spielersicht:")
    zeigeSpielersicht(feld)
print(f"Super, du hast alle Schiffe zertört und hast dafür {GebrauchteSchuesse} Schüsse gebraucht")