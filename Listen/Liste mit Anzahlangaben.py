o = 0
l = []
while o < 1:
    i = input("Möchtest du etwas auf deine Einkaufsliste schreiben? (Ja/Nein): ")
    i = i.upper()
    i = i.replace(" ", "")
    i = i.replace(".", "")
    while i == "JA":
        hz = input("Was möchtest du hinzufügen? ")
        hz = hz.lower()
        if hz in l:
            a = input("Wie oft? ")
            a = a.replace(" ", "")
        else:
            if hz in l:
                m = input("Das hast du bereits notiert. Möchtest du mehr davon? (Ja/Nein): ")
                m = m.upper()
                m = m.replace(" ", "")
                m = m.replace(".", "")
                if m == "JA":
                    am = input("Wie oft? ")
                    am = am.replace(" ", "")
                    a = int(a) + int(am)
                    l.append(hz)
                    l.insert(-1, a)
                    print(l)
                else:
                    print("Dann nich. ")             
            else:
                l.append(hz)
                l.insert(-1, a)
                print(l)
            i = input("Möchtest du noch etwas hinzufügen? (Ja/Nein): ")
            i = i.upper()
            i = i.replace(" ", "")
            i = i.replace(".", "")
        print(l)
    
    e = input("Möchtest du etwas entfernen? (Ja/Nein): ")
    i = "ja"
    e = e.upper()
    e = e.replace(" ", "")
    e = e.replace(".", "")
    while e == "JA":
        ent = input("Was möchtest du entfernen? ")
        ent = ent.lower()
        if ent in l:
            l.remove(ent)
        else:
            print("Ist nicht vorhanden.")
        print(l)
        e = input("Möchtest du noch etwas entfernen? (Ja/Nein): ")
        e = e.upper()
        e = e.replace(" ", "")
        e = e.replace(".", "")
    print("Dann halt nich, Opfer :((( ")