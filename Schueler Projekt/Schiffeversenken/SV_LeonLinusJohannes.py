from random import randint

'''
Author: Leon, Linus, Johannes
'''

# Groesse des Feldes
gewuenschteFeldGroesse = False
while gewuenschteFeldGroesse is False:
    try:
        gewuenschteFeldGroesse = int(input("Feldgroesse: "))
    except ValueError:
        print('Bitte nur ganze Zahlen eingeben!')
FeldGroesse = 0
ZeilenGroesse = 0
zeile = []
feld = []


# Das Zeug ausm Testmodul
def zeigeSpielersicht(feld):
    i = 0

    AnzahlZahlen = 0
    Zahl = 1
    Zahlen = [" "]

    while AnzahlZahlen < gewuenschteFeldGroesse:
        Zahlen.append(" ")
        Zahlen.append(Zahl)  # type: ignore
        Zahl += 1
        AnzahlZahlen += 1
    print(*Zahlen, sep="")  # Schönes Ausgeben der Listen

    while i < gewuenschteFeldGroesse:
        j = 0
        zeilentext = str(i + 1) + ' '
        while j < gewuenschteFeldGroesse:
            if feld[i][j] == 'S' or feld[i][j] == 'A':  # Schiffe/Abstandsfelder nicht zeigen
                zeilentext += '~ '
            else:
                zeilentext += feld[i][j] + ' '
            j = j + 1
        i = i + 1
        print(zeilentext)
    print('')  # Leerzeile nach dem Feld


def zeigeComputersicht(feld):
    i = 0

    AnzahlZahlen = 0
    Zahl = 1
    Zahlen = [" "]

    while AnzahlZahlen < gewuenschteFeldGroesse:
        Zahlen.append(" ")
        Zahlen.append(Zahl)  # type: ignore
        Zahl += 1
        AnzahlZahlen += 1
    print(*Zahlen, sep="")  # Schönes Ausgeben der Listen

    while i < gewuenschteFeldGroesse:
        j = 0
        zeilentext = str(i + 1) + ' '
        while j < gewuenschteFeldGroesse:
            if feld[i][j] == 'A':
                zeilentext += '~ '  #######
            else:
                zeilentext += feld[i][j] + ' '
            j = j + 1
        i = i + 1
        print(zeilentext)
    print('')  # Leerzeile nach dem Feld


# Hier ist wieder normales Programm
while FeldGroesse < gewuenschteFeldGroesse:
    zeile = []
    ZeilenGroesse = 0
    while ZeilenGroesse < gewuenschteFeldGroesse:
        zeile.append("~")
        ZeilenGroesse += 1
    zeile.append(" ")
    zeile.append(" ")
    feld.append(zeile)
    # zeile = []
    FeldGroesse += 1
feld.append(zeile)

# Ausgabe der Spielfelder
# print(feld) Einzeilige Ausgabe zur Überpruefung
print("Spielersicht:")
zeigeSpielersicht(feld)

print("Computersicht:")
zeigeComputersicht(feld)

# Zufallsverteilung der 1er-Schiffchen
Vorhandene1erSchiffe = 0
AnzahlSFelder = 0
AnzahlSchiffe = False
while AnzahlSchiffe is False:
    try: 
        AnzahlSchiffe = int(input("Anzahl der Einer-Schiffchen: "))
    except ValueError:
        print('Bitte nur ganze Zahlen eingeben!')
    
# Hilfsvariablen für DIE FORMEL
f = float(FeldGroesse / 2)
i = int(f)
# DIE FORMEL
Ichgebauf = 0
while AnzahlSchiffe > f ** 2:
    print("Das sind zuviele Schiffe, try again :( ")
    print(AnzahlSchiffe)
    AnzahlSchiffe = False
    while AnzahlSchiffe is False:
        try:
            AnzahlSchiffe = int(input("Anzahl der Einer-Schiffchen: "))
        except ValueError:
            print('Bitte nur ganze Zahlen eingeben!')
            
while AnzahlSchiffe > Vorhandene1erSchiffe and Ichgebauf <= 100:
    SchiffZeile = randint(0, FeldGroesse - 1)
    SchiffSpalte = randint(0, FeldGroesse - 1)
    Ichgebauf += 1
    # print(SchiffZeile) #Zur Überpruefung bei Errors
    # print(SchiffSpalte) #Zur Überpruefung bei Errors

    # Die oberste Zeile
    if SchiffZeile == 0 and feld[SchiffZeile][SchiffSpalte] != "S" and feld[SchiffZeile][SchiffSpalte] != "A":
        feld[SchiffZeile][SchiffSpalte] = "S"

        feld[SchiffZeile][SchiffSpalte + 1] = "A"
        feld[SchiffZeile + 1][SchiffSpalte] = "A"
        feld[SchiffZeile + 1][SchiffSpalte + 1] = "A"
        feld[SchiffZeile + 1][SchiffSpalte - 1] = "A"
        
        if SchiffSpalte > 0:
            feld[SchiffZeile][SchiffSpalte - 1] = "A"

        AnzahlSFelder += 1
        Vorhandene1erSchiffe += 1

    # Die unterste Zeile
    if SchiffZeile == FeldGroesse - 1 and feld[SchiffZeile][SchiffSpalte] != "S" and feld[SchiffZeile][SchiffSpalte] != "A":
        feld[SchiffZeile][SchiffSpalte] = "S"

        feld[SchiffZeile][SchiffSpalte + 1] = "A"
        feld[SchiffZeile - 1][SchiffSpalte] = "A"
        feld[SchiffZeile - 1][SchiffSpalte - 1] = "A"
        feld[SchiffZeile - 1][SchiffSpalte + 1] = "A"
        if SchiffSpalte > 0:
            feld[SchiffZeile][SchiffSpalte - 1] = "A"

        AnzahlSFelder += 1
        Vorhandene1erSchiffe += 1

    if feld[SchiffZeile][SchiffSpalte] != "S" and feld[SchiffZeile][SchiffSpalte] != "A":
        if feld[SchiffZeile - 1][SchiffSpalte] != "S":
            if feld[SchiffZeile - 1][SchiffSpalte - 1] != "S":
                if feld[SchiffZeile][SchiffSpalte - 1] != "S":
                    if feld[SchiffZeile + 1][SchiffSpalte - 1] != "S":
                        if feld[SchiffZeile + 1][SchiffSpalte] != "S":
                            if feld[SchiffZeile + 1][SchiffSpalte + 1] != "S":
                                if feld[SchiffZeile][SchiffSpalte + 1] != "S":
                                    if feld[SchiffZeile - 1][SchiffSpalte + 1] != "S":
                                        feld[SchiffZeile][SchiffSpalte] = "S"
                                        
                                        feld[SchiffZeile][SchiffSpalte - 1] = "A"
                                        feld[SchiffZeile][SchiffSpalte + 1] = "A"
                                        feld[SchiffZeile - 1][SchiffSpalte] = "A"
                                        feld[SchiffZeile - 1][SchiffSpalte - 1] = "A"
                                        feld[SchiffZeile - 1][SchiffSpalte + 1] = "A"
                                        feld[SchiffZeile + 1][SchiffSpalte] = "A"
                                        feld[SchiffZeile + 1][SchiffSpalte - 1] = "A"
                                        feld[SchiffZeile + 1][SchiffSpalte + 1] = "A"

                                        AnzahlSFelder += 1
                                        Vorhandene1erSchiffe += 1

# Zufallsverteilung der 2er-Schiffchen
Vorhandene2erSchiffe = 0
Anzahl2erSFelder = 0
Anzahl2erSchiffe = False
while Anzahl2erSchiffe is False:
    try:
        Anzahl2erSchiffe = int(input("Anzahl der 2er-Schiffchen: "))
    except ValueError:
        print('Bitte nur ganze Zahlen eingeben!')
     
Ichgebauf = 0

while Anzahl2erSchiffe > Vorhandene2erSchiffe and Ichgebauf <= 1000:
    Ichgebauf += 1
    
    # horizontal oder vertikal
    hoderv = randint(0, 1)
    
    # 1 ist vertikal
    if hoderv == 1:
        SchiffZeile = randint(1, FeldGroesse - 1)
        SchiffSpalte = randint(0, FeldGroesse - 1)
        
        # Die oberste Zeile
        if SchiffZeile == 1 and feld[SchiffZeile][SchiffSpalte] != "S" and feld[SchiffZeile][SchiffSpalte] != "A":
            if feld[SchiffZeile - 1][SchiffSpalte] != "S" and feld[SchiffZeile - 1][SchiffSpalte] != "A":
                feld[SchiffZeile][SchiffSpalte] = "S"
                feld[SchiffZeile - 1 ][SchiffSpalte] = "S"

                feld[SchiffZeile][SchiffSpalte + 1] = "A"
                feld[SchiffZeile + 1][SchiffSpalte] = "A"
                feld[SchiffZeile + 1][SchiffSpalte + 1] = "A"
                feld[SchiffZeile - 1][SchiffSpalte + 1] = "A"

                if SchiffSpalte > 0:
                    feld[SchiffZeile][SchiffSpalte - 1] = "A"
                    feld[SchiffZeile + 1][SchiffSpalte - 1] = "A"
                    feld[SchiffZeile - 1][SchiffSpalte - 1] = "A"
                    
                Anzahl2erSFelder += 2
                Vorhandene2erSchiffe += 1

        # Die unterste Zeile
        if SchiffZeile == FeldGroesse - 1 and feld[SchiffZeile][SchiffSpalte] != "S" and feld[SchiffZeile][SchiffSpalte] != "A":
            if feld[SchiffZeile + 1][SchiffSpalte] != "S" and feld[SchiffZeile + 1][SchiffSpalte] != "A":
                feld[SchiffZeile][SchiffSpalte] = "S"
                feld[SchiffZeile - 1 ][SchiffSpalte] = "S"

                feld[SchiffZeile][SchiffSpalte + 1] = "A"
                feld[SchiffZeile][SchiffSpalte - 1] = "A"
                feld[SchiffZeile - 2][SchiffSpalte] = "A"
                feld[SchiffZeile - 1][SchiffSpalte + 1] = "A"
                feld[SchiffZeile - 2][SchiffSpalte + 1] = "A"
                feld[SchiffZeile - 1][SchiffSpalte - 1] = "A"
                feld[SchiffZeile - 2][SchiffSpalte - 1] = "A"

                Anzahl2erSFelder += 2
                Vorhandene2erSchiffe += 1
        
        if feld[SchiffZeile][SchiffSpalte] != "S" and feld[SchiffZeile][SchiffSpalte] != "A":
            if feld[SchiffZeile - 1][SchiffSpalte] != "S":
                if feld[SchiffZeile - 1][SchiffSpalte - 1] != "S":
                    if feld[SchiffZeile][SchiffSpalte - 1] != "S":
                        if feld[SchiffZeile + 1][SchiffSpalte - 1] != "S":
                            if feld[SchiffZeile + 1][SchiffSpalte] != "S":
                                if feld[SchiffZeile + 1][SchiffSpalte + 1] != "S":
                                    if feld[SchiffZeile][SchiffSpalte + 1] != "S":
                                        if feld[SchiffZeile - 1][SchiffSpalte + 1] != "S":
                                            if feld[SchiffZeile - 2][SchiffSpalte - 1] != "S":
                                                if feld[SchiffZeile - 2][SchiffSpalte] != "S":
                                                    if feld[SchiffZeile - 2][SchiffSpalte + 1] != "S":
                                            
                                                        # Abstandsfelder
                                                        feld[SchiffZeile][SchiffSpalte] = "S"
                                                        feld[SchiffZeile - 1 ][SchiffSpalte] = "S"
                                                        
                                                        feld[SchiffZeile][SchiffSpalte - 1] = "A"
                                                        feld[SchiffZeile][SchiffSpalte + 1] = "A"
                                                        feld[SchiffZeile - 2][SchiffSpalte] = "A"
                                                        feld[SchiffZeile - 2][SchiffSpalte - 1] = "A"
                                                        feld[SchiffZeile - 2][SchiffSpalte + 1] = "A"
                                                        feld[SchiffZeile - 1][SchiffSpalte - 1] = "A"
                                                        feld[SchiffZeile - 1][SchiffSpalte + 1] = "A"
                                                        feld[SchiffZeile + 1][SchiffSpalte - 1] = "A"
                                                        feld[SchiffZeile + 1][SchiffSpalte + 1] = "A"
                                                        feld[SchiffZeile + 1][SchiffSpalte] = "A"
                                                        
                                                        Anzahl2erSFelder += 2
                                                        Vorhandene2erSchiffe += 1
    
    # 0 ist horizontal
    elif hoderv == 0:
        SchiffZeile = randint(0, FeldGroesse - 1)
        SchiffSpalte = randint(0, FeldGroesse - 2)
        
        # Die oberste Zeile
        if SchiffZeile == 0 and feld[SchiffZeile][SchiffSpalte] != "S" and feld[SchiffZeile][SchiffSpalte] != "A":
            if feld[SchiffZeile][SchiffSpalte + 1] != "S" and feld[SchiffZeile][SchiffSpalte + 1] != "A":
                feld[SchiffZeile][SchiffSpalte] = "S"
                feld[SchiffZeile][SchiffSpalte + 1] = "S"

                feld[SchiffZeile][SchiffSpalte + 2] = "A"
                feld[SchiffZeile + 1][SchiffSpalte] = "A"
                feld[SchiffZeile + 1][SchiffSpalte + 1] = "A"
                feld[SchiffZeile + 1][SchiffSpalte + 2] = "A"

                if SchiffSpalte > 0:
                    feld[SchiffZeile][SchiffSpalte - 1] = "A"
                    feld[SchiffZeile + 1][SchiffSpalte - 1] = "A"
                Anzahl2erSFelder += 2
                Vorhandene2erSchiffe += 1

        # Die unterste Zeile
        if SchiffZeile == FeldGroesse - 1 and feld[SchiffZeile][SchiffSpalte] != "S" and feld[SchiffZeile][SchiffSpalte] != "A":
            feld[SchiffZeile][SchiffSpalte] = "S"
            feld[SchiffZeile][SchiffSpalte + 1] = "S"

            feld[SchiffZeile][SchiffSpalte + 2] = "A"
            feld[SchiffZeile][SchiffSpalte - 1] = "A"
            feld[SchiffZeile - 1][SchiffSpalte] = "A"
            feld[SchiffZeile - 1][SchiffSpalte - 1] = "A"
            feld[SchiffZeile - 1][SchiffSpalte + 1] = "A"
            feld[SchiffZeile - 1][SchiffSpalte + 2] = "A"
            Anzahl2erSFelder += 2
            Vorhandene2erSchiffe += 1
        
        if feld[SchiffZeile][SchiffSpalte] != "S" and feld[SchiffZeile][SchiffSpalte] != "A":
            if feld[SchiffZeile - 1][SchiffSpalte] != "S":
                if feld[SchiffZeile - 1][SchiffSpalte - 1] != "S":
                    if feld[SchiffZeile][SchiffSpalte - 1] != "S":
                        if feld[SchiffZeile + 1][SchiffSpalte - 1] != "S":
                            if feld[SchiffZeile + 1][SchiffSpalte] != "S":
                                if feld[SchiffZeile + 1][SchiffSpalte + 1] != "S":
                                    if feld[SchiffZeile][SchiffSpalte + 1] != "S":
                                        if feld[SchiffZeile + 1][SchiffSpalte + 2] != "S":
                                            if feld[SchiffZeile][SchiffSpalte + 2] != "S":
                                                if feld[SchiffZeile - 1][SchiffSpalte + 1] != "S":
                                                    if feld[SchiffZeile - 1][SchiffSpalte + 2] != "S":
                                                        # Abstandsfelder
                                                        feld[SchiffZeile][SchiffSpalte] = "A"
                                                        feld[SchiffZeile][SchiffSpalte + 2] = "A"
                                                        feld[SchiffZeile][SchiffSpalte - 1] = "A"
                                                        feld[SchiffZeile + 1][SchiffSpalte] = "A"
                                                        feld[SchiffZeile + 1][SchiffSpalte + 1] = "A"
                                                        feld[SchiffZeile + 1][SchiffSpalte + 2] = "A"
                                                        feld[SchiffZeile + 1][SchiffSpalte - 1] = "A"
                                                        feld[SchiffZeile - 1][SchiffSpalte] = "A"
                                                        feld[SchiffZeile - 1][SchiffSpalte + 1] = "A"
                                                        feld[SchiffZeile - 1][SchiffSpalte + 2] = "A"
                                                        feld[SchiffZeile - 1][SchiffSpalte - 1] = "A"

                                                        # Schiffsplatzierung
                                                        feld[SchiffZeile][SchiffSpalte] = "S"
                                                        feld[SchiffZeile][SchiffSpalte + 1] = "S"
                                                        Anzahl2erSFelder += 2
                                                        Vorhandene2erSchiffe += 1
    
print("Computersicht:")
zeigeComputersicht(feld)

print(f"Aufgrund der Zufallsverteilung wurden {Vorhandene2erSchiffe} 2er- und {Vorhandene1erSchiffe} 1er-Schiffe platziert.")

# Beschuss
getroffeneFelder = 0
GebrauchteSchuesse = 0
SchussZeile = False
SchussSpalte = False

while getroffeneFelder < AnzahlSFelder + Anzahl2erSFelder:
    while SchussZeile is False:
        try:
            SchussZeile = int(input("Zeile: "))
            if SchussZeile < 1:
                print('Zahl muss groesser als 0 sein.')
                SchussZeile = False
        except ValueError:
            print('Bitte nur ganze Zahlen eingeben!')

    # whileschleife sorgt dafür, dass man keine zu grosse Zahl eingeben kann und so ein Error verhindert wird
    while SchussZeile > gewuenschteFeldGroesse:
        print(f"Deine eingegebene Zahl ist zu gross. Die Feldgroesse betraegt nur {gewuenschteFeldGroesse} Felder.")
        SchussZeile = False
        while SchussZeile is False:
            try:
                SchussZeile = int(input("Zeile: "))
                if SchussZeile < 1:
                    print('Zahl muss groesser als 0 sein.')
                    SchussZeile = False
            except ValueError:
                print('Bitte nur ganze Zahlen eingeben!')

    while SchussSpalte is False:
        try:
            SchussSpalte = int(input("Spalte: "))
            if SchussSpalte < 1:
                print('Zahl muss groesser als 0 sein.')
                SchussSpalte = False
        except ValueError:
            print('Bitte nur ganze Zahlen eingeben!')
    print('')
    
    # whileschleife sorgt dafür, dass man keine zu grosse Zahl eingeben kann und so ein Error verhindert wird
    while SchussSpalte > gewuenschteFeldGroesse:
        print(f"Deine eingegebene Zahl ist zu gross. Die Feldgroesse betraegt nur {gewuenschteFeldGroesse} Felder.")
        SchussSpalte = False
        while SchussSpalte is False:
            try:
                SchussSpalte = int(input("Spalte: "))
                if SchussSpalte < 1:
                    print('Zahl muss groesser als 0 sein.')
                    SchussSpalte = False
            except ValueError:
                print('Bitte nur ganze Zahlen eingeben!')
        print('')

    SchussZeile -= 1
    SchussSpalte -= 1
    
    # Treffer als "T" markieren

        # Unterste Zeile
    if SchussZeile == FeldGroesse and feld[SchussZeile][SchussSpalte] == "S":
        feld[SchussZeile][SchussSpalte] = "T"
        getroffeneFelder += 1
        GebrauchteSchuesse += 1
        
        if feld[SchussZeile - 1][SchussSpalte] == "S":
            print("Treffer! ")
        elif feld[SchussZeile][SchussSpalte + 1] == "S":
            print("Treffer! ")
        elif feld[SchussZeile][SchussSpalte - 1] == "S":
            print("Treffer! ")
        else:
            print('Treffer versenkt! ')


        # Oberste Zeile
    elif SchussZeile == 0 and feld[SchussZeile][SchussSpalte] == "S":
        feld[SchussZeile][SchussSpalte] = "T"
        getroffeneFelder += 1
        GebrauchteSchuesse += 1
        
        if feld[SchussZeile + 1][SchussSpalte] == "S":
            print("Treffer! ")
        elif feld[SchussZeile][SchussSpalte + 1] == "S":
            print("Treffer! ")
        elif feld[SchussZeile][SchussSpalte - 1] == "S":
            print("Treffer! ")
        else:
            print('Treffer versenkt! ')
        
        # Alle Anderen Zeilen
    elif feld[SchussZeile][SchussSpalte] == "S":
        feld[SchussZeile][SchussSpalte] = "T"
        getroffeneFelder += 1
        GebrauchteSchuesse += 1
        
        if feld[SchussZeile + 1][SchussSpalte] == "S":
            print("Treffer! ")
        elif feld[SchussZeile - 1][SchussSpalte] == "S":
            print("Treffer! ")
        elif feld[SchussZeile][SchussSpalte + 1] == "S":
            print("Treffer! ")
        elif feld[SchussZeile][SchussSpalte - 1] == "S":
            print("Treffer! ")
        else:
            print('Treffer versenkt! ')

    # Fehlschüsse als solche markieren
    elif feld[SchussZeile][SchussSpalte] == "~" or feld[SchussZeile][SchussSpalte] == "A":
        feld[SchussZeile][SchussSpalte] = "X"
        GebrauchteSchuesse += 1
        print('Leider daneben. Versuch es nocheinmal.')

    SchussZeile = False
    SchussSpalte = False

    print("Spielersicht:")
    zeigeSpielersicht(feld)


# Statistik des Spiels
def SpielStatistik():
    Trefferquote = (getroffeneFelder / GebrauchteSchuesse) * 100
    Feld = FeldGroesse

    print(f'''
================================================
| Spiel-Statistik:
|     
| Trefferquote:            {Trefferquote: .2f}%
| Platzierte 1er-Schiffe:   {Vorhandene1erSchiffe}
| Platzierte 2er-Schiffe:   {Vorhandene2erSchiffe}
| Gewaehlte Feldgroesse:    {Feld}
| Gebrauchte Schuesse:      {GebrauchteSchuesse}
================================================
''')

SpielStatistik()
