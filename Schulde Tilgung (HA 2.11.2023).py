# Eingabe
Schulden = float(input("Schulden zu Beginn: "))
Zinssatz = float(input("Zinssatz in Prozent: "))
Tilgung = float(input("Tilgung pro Monat: "))
zins = Zinssatz / 100
# Verarbeitung
jahr = 0
while Schulden > 0:
    Schulden = (Schulden + zins)  - Tilgung
    jahr = jahr + 1

# Ausgabe
print("Du brauchst ", jahr,"Jahre um deine Schulden zu Tilgen.") 