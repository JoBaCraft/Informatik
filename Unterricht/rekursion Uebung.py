def kapital(n):
    return 1000 if n==0 else kapital(n-1)*1.05

def medmenge(n):
    return 5 if n==0 else medmenge(n-1)*0.6+5


#2D
def umfang(n, m):
    return 4*m if n==0 else umfang(n-1, m)+2*m

def flaecheninhalt(n, m):
    return m**2 if n==0 else 3*flaecheninhalt(n-1, m/3)+m**2


#3D
def volumen(n, m):
    return m**3 if n==0 else volumen(n-1,m)+(5**n)*(m/(3**n))**3

def oberflaeche(n, m):
    return 6*m**2 if n==0 else oberflaeche(n-1,m)+4*(5**n)*(m/(3**n))**2

def kantenlaenge(n, m):
    return 12*m if n==0 else kantenlaenge(n-1,m)+12*(5**n)*m/(3**n)


print(f'''
Kapital: {kapital(5):.2f} Euro
Menge Medizin: {medmenge(5):.2f}mg
Umfang: {umfang(3, 3):.2f}cm
Flaecheninhalt: {flaecheninhalt(3, 3):.2f}cm^2
Volumen: {volumen(3, 3):.2f}cm^3
Oberflaeche: {oberflaeche(3, 3):.2f}cm^2
Kantenlaenge: {kantenlaenge(3, 3):.2f}cm
''')