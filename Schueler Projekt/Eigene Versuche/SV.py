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

print("Computersicht:")
zeigeComputersicht(feld)
    
#Beschuss

#Achtung Fehler
for i, textstelle in sum(feld, []) == "S":
#Endet hier
    
    zeile = int(input("Zeile: "))
    spalte = int(input("Spalte: "))

    if feld[zeile - 1][spalte - 1] == "S":
        feld[zeile - 1][spalte - 1] = "T"
    
    elif feld[zeile - 1][spalte - 1] == "~":
        feld[zeile - 1][spalte - 1] = "X"
    
    print("Spielersicht:")
    zeigeSpielersicht(feld)