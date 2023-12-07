from testModul import zeigeSpielersicht, zeigeComputersicht
from random import randint

#Aufstellen der einzelnen Reihen
zeile1 = ['~','~','~','~','~','~','~','~']
zeile2 = ['~','~','~','~','~','~','~','~']
zeile3 = ['~','~','~','~','~','~','~','~']
zeile4 = ['~','~','~','~','~','~','~','~']
zeile5 = ['~','~','~','~','~','~','~','~']
zeile6 = ['~','~','~','~','~','~','~','~']
zeile7 = ['~','~','~','~','~','~','~','~']
zeile8 = ['~','~','~','~','~','~','~','~']

#Zusammenfuegen der Reihen zu einem Feld
feld = [zeile1, zeile2, zeile3, zeile4, zeile5, zeile6, zeile7, zeile8]

#Ausgabe der Spielfelder
print("Spielersicht:")
zeigeSpielersicht(feld)

print("Computersicht:")
zeigeComputersicht(feld)


#Zufallsverteilung der Schiffchen
VorhandeneSchiffe = 0
AnzahlSchiffe = int(input("Anzahl der Einer-Schiffchen: "))
while AnzahlSchiffe > VorhandeneSchiffe:
    SchiffZeile = randint(0, 7)
    SchiffSpalte = randint(0, 7)
    if feld[SchiffZeile][SchiffSpalte] != "S":
        feld[SchiffZeile][SchiffSpalte] = "S"
        VorhandeneSchiffe += 1

        
        if feld[SchiffZeile-1][SchiffSpalte] != "S" or feld[SchiffZeile-1][SchiffSpalte] >= 8:      # type: ignore
           if feld[SchiffZeile-1][SchiffSpalte-1] != "S" or feld[SchiffZeile-1][SchiffSpalte-1] >= 8:    # type: ignore
                if feld[SchiffZeile][SchiffSpalte-1] != "S" or feld[SchiffZeile][SchiffSpalte-1] >= 8:    # type: ignore
                    if feld[SchiffZeile+1][SchiffSpalte-1] != "S" or feld[SchiffZeile+1][SchiffSpalte-1] >= 8:    # type: ignore
                        if feld[SchiffZeile+1][SchiffSpalte] != "S" or feld[SchiffZeile+1][SchiffSpalte] >= 8:    # type: ignore
                            if feld[SchiffZeile+1][SchiffSpalte+1] != "S" or feld[SchiffZeile+1][SchiffSpalte+1] >= 8:    # type: ignore
                                if feld[SchiffZeile][SchiffSpalte+1] != "S" or feld[SchiffZeile][SchiffSpalte+1] >= 8:    # type: ignore
                                    if feld[SchiffZeile-1][SchiffSpalte+1] != "S" or feld[SchiffZeile-1][SchiffSpalte+1] >= 8:       # type: ignore
                                        feld[SchiffZeile][SchiffSpalte] = 'A'


print("Computersicht:")
zeigeComputersicht(feld)
    
#Beschuss

zeile = int(input("Zeile: "))
spalte = int(input("Spalte: "))
if feld[zeile - 1][spalte - 1] == "S":
    feld[zeile - 1][spalte - 1] = "T"
    print('Treffer')
    print('')  
    
elif feld[zeile - 1][spalte - 1] == "~":
    feld[zeile - 1][spalte - 1] = "X"
    print('Daneben')
    print('')
    
print("Spielersicht:")
zeigeSpielersicht(feld)