from testModulLeon import zeigeSpielersicht, zeigeComputersicht
from random import randint

#Größe des Feldes
gewuenschteFeldGroesse = int(input("Feldgroesse: "))
FeldGroesse = 0
#for FeldGroesse in range(gewuenschteFeldGroesse):

#while FeldGroesse < gewuenschteFeldGroesse:
    #ZeilenGroesse = 0
   # while ZeilenGroesse < gewuenschteFeldGroesse:
       # zeile
    

#Aufstellen der einzelnen Reihen
zeile1 = ['~','~','~','~','~','~','~','~'," "]
zeile2 = ['~','~','~','~','~','~','~','~'," "]
zeile3 = ['~','~','~','~','~','~','~','~'," "]
zeile4 = ['~','~','~','~','~','~','~','~'," "]
zeile5 = ['~','~','~','~','~','~','~','~'," "]
zeile6 = ['~','~','~','~','~','~','~','~'," "]
zeile7 = ['~','~','~','~','~','~','~','~'," "]
zeile8 = ['~','~','~','~','~','~','~','~'," "]
zeile9 = ['~','~','~','~','~','~','~','~'," "]
zeile10 = ['~','~','~','~','~','~','~','~'," "]

#Zusammenfuegen der Reihen zu einem Feld
feld = [zeile1, zeile2, zeile3, zeile4, zeile5, zeile6, zeile7, zeile8, zeile9]

#Ausgabe der Spielfelder
print("Spielersicht:")
zeigeSpielersicht(feld)

print("Computersicht:")
zeigeComputersicht(feld)


#Zufallsverteilung der Schiffchen
VorhandeneSchiffe = 0
AnzahlSFelder = 0
AnzahlSchiffe = 1#int(input("Anzahl der Einer-Schiffchen: "))
while AnzahlSchiffe > VorhandeneSchiffe:
    SchiffZeile = 7#randint(0, 7)
    SchiffSpalte = 7#randint(0, 7)
    print(SchiffSpalte)
    print(SchiffZeile)
    if feld[SchiffZeile][SchiffSpalte] != "S":
        if feld[SchiffZeile-1][SchiffSpalte] != "S": #or feld[SchiffZeile-1] >= 7:
           if feld[SchiffZeile-1][SchiffSpalte-1] != "S": #or feld[SchiffZeile-1] >= 7 or feld[SchiffSpalte-1] >= 7:
                if feld[SchiffZeile][SchiffSpalte-1] != "S" or feld[SchiffSpalte-1] >= 7: # type: ignore
                    if feld[SchiffZeile+1][SchiffSpalte-1] != "S" or feld[SchiffZeile+1] >=7 or feld[SchiffSpalte-1] >= 7: # type: ignore
                        if feld[SchiffZeile+1][SchiffSpalte] != "S" or feld[SchiffZeile+1] >=7:  # type: ignore
                            if feld[SchiffZeile+1][SchiffSpalte+1] != "S":# or feld[SchiffZeile+1] >=7 or feld[SchiffSpalte+1] >= 7:
                                if feld[SchiffZeile][SchiffSpalte+1] != "S": #or feld[SchiffSpalte+1] >= 7:
                                    if feld[SchiffZeile-1][SchiffSpalte+1] != "S": #orfeld[SchiffZeile-1] >=7 or feld[SchiffSpalte+1] >= 7:
                
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
    
print("Computersicht:")
zeigeComputersicht(feld)
    
#Beschuss

#Achtung Fehler
#for i, textstelle in sum(feld, []) == "S":
#Endet hier
getroffenenFelder = 0
GebrauchteSchuesse = 0
while getroffenenFelder < AnzahlSFelder:
    zeile = int(input("Zeile: "))
    spalte = int(input("Spalte: "))

    if feld[zeile - 1][spalte - 1] == "S":
        feld[zeile - 1][spalte - 1] = "T"
        getroffenenFelder += 1
        GebrauchteSchuesse += 1
    
    elif feld[zeile - 1][spalte - 1] == "~":
       feld[zeile - 1][spalte - 1] = "X"
       GebrauchteSchuesse += 1
    
    print("Spielersicht:")
    zeigeSpielersicht(feld)
    print(GebrauchteSchuesse)
