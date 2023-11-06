# Eingabe
Schulden = float(input("Schulden in Euro zu Beginn: "))
Zinssatz = float(input("Zinssatz in Prozent: "))
Tilgung = float(input("Tilgung in Euro pro Monat: "))
zins = Zinssatz / 100
# Verarbeitung
jahr = 0
while Schulden > 0:
    Schulden = (Schulden + zins)  - (Tilgung * 12)
    jahr = jahr + 1

# Ausgabe
print("Du brauchst ", jahr,"Jahre um deine Schulden zu Tilgen.") 