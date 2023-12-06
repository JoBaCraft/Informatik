from ausgabeModul import zeigeSpielersicht, zeigeComputersicht

#Aufstellen der einzelnen Reihen
zeile1 = ['~','~','~','~','~','~','~','~']
zeile2 = ['~','S','~','X','S','~','T','~']
zeile3 = ['~','X','~','~','~','~','T','~']
zeile4 = ['~','~','~','S','~','~','T','~']
zeile5 = ['S','~','~','~','~','~','S','~']
zeile6 = ['~','~','~','~','~','~','~','S']
zeile7 = ['~','~','S','~','T','~','~','~']
zeile8 = ['S','~','~','~','~','~','~','~']

#Zusammenfuegen der Reihen zu einem Feld
feld = [zeile1, zeile2, zeile3, zeile4, zeile5, zeile6, zeile7, zeile8]

#Ausgabe der Spielfelder
print("Spielersicht:")
zeigeSpielersicht(feld)

print("Computersicht:")
zeigeComputersicht(feld)