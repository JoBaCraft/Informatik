from random import randint

'''
Author: Johannes
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
while FeldGroesse < gewuenschteFeldGroesse:
    zeile = []
    ZeilenGroesse = 0
    while ZeilenGroesse < gewuenschteFeldGroesse:
        zeile.append("~")
        ZeilenGroesse += 1
    zeile.append(" ")
    zeile.append(" ")
    feld.append(zeile)
    FeldGroesse += 1
feld.append(zeile)

def zeigeSpielersicht(feld):
    i = 0

    AnzahlZahlen = 0
    Zahl = 1
    Zahlen = [" "]

    while AnzahlZahlen < gewuenschteFeldGroesse:
        Zahlen.append(Zahl)  # type: ignore
        Zahl += 1
        AnzahlZahlen += 1
    print(*Zahlen, sep=" ")  # Schönes Ausgeben der Listen

    while i < gewuenschteFeldGroesse:
        j = 0
        zeilentext = str(i + 1) + ' '
        while j < gewuenschteFeldGroesse:
            if feld[i][j] == 'S' or feld[i][j] == 'A':  # Schiffe/Abstandsfelder nicht zeigen
                zeilentext += '~ '
            else:
                zeilentext += feld[i][j] + ' '
            j += 1
        i += 1
        print(zeilentext)
    print('')  # Leerzeile nach dem Feld


def zeigeComputersicht(feld):
    i = 0

    AnzahlZahlen = 0
    Zahl = 1
    Zahlen = [" "]

    while AnzahlZahlen < gewuenschteFeldGroesse:
        Zahlen.append(Zahl)  # type: ignore
        Zahl += 1
        AnzahlZahlen += 1
    print(*Zahlen, sep=" ")  # Schönes Ausgeben der Listen

    while i < gewuenschteFeldGroesse:
        j = 0
        zeilentext = str(i + 1) + ' '
        while j < gewuenschteFeldGroesse:
            if feld[i][j] == 'A':
                zeilentext += 'A '
            else:
                zeilentext += feld[i][j] + ' '
            j += 1
        i += 1
        print(zeilentext)
    print('')  # Leerzeile nach dem Feld


print("Spielersicht:")
zeigeSpielersicht(feld)

print("Computersicht:")
zeigeComputersicht(feld)


def Schiffsplatzierung(feld, SchiffsGroesse, SchiffsAnzahl):
    if 1 > 2:
        print('warum?')


Schiffsplatzierung(feld, 1, 6)
