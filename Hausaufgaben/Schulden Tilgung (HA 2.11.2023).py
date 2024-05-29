# Eingabe
Schulden = float(input("Schulden in Euro zu Beginn: "))
Zinssatz = float(input("Zinssatz in Prozent: "))
Tilgung = float(input("Tilgung in Euro pro Monat: "))
Extrarükzahlungen = float(input("Extrarückzahlunge in Euro (gesamt): "))
zins = (Zinssatz / 100) + 1
# Verarbeitung
Schulden = Schulden - Extrarükzahlungen
jahr = 0
while Schulden > 0:
    Schulden = (Schulden * zins)  - (Tilgung * 12)
    jahr += 1

# Ausgabe
print(f"Du brauchst {jahr} Jahre um deine Schulden zu Tilgen.") 