def kapital(n):
    if n == 0:
        return 1000
    else:
        return 1.05 * kapital(n-1)

def medmeng(n):
    if n == 0:
        return 5
    else:
        return 0.6 * medmeng(n-1) + 5



# Quadratpflanze 2D
def umfang(n, m):
    if n == 0:
        return 4 * m
    else:
        return umfang(n-1, m) + 2*m
    
    
def flaecheninhalt(n, m):
    if n == 0:
        return m ** 2
    else:
        return flaecheninhalt(n-1, m) + m**2 /(3**n)




#Quadratplfanze 3D
def volumen_3d(n,m):
    if n == 0:
        return m ** 3
    else:
        return volumen_3d(n-1,m) + 5 ** n * (m/(3**n)) ** 3
    
def oberfläche(n,m):
    if n == 0:
        return 6 * m **2
    else:
        return oberfläche(n-1,m) + 4 * 5**n * (m/(3**n))**2

def kantenlaenge(n,m):
    if n == 0:
        return 12 * m
    else:
        return kantenlaenge(n-1,m) + 12* 5**n * m/ (3**n)







# Mathe Problem
def gcd(a, b):
 
    if (a == 0):
        return b
    return gcd(b % a, a)
 

def euler_totient(n):
    if n == 1:
        return 1
    # Initialize the count of coprime numbers to 0
    count = 0
    # Iterate from 1 to n-1
    for i in range(1, n):
        # Check if i and n are coprime using gcd
        if gcd(i, n) == 1:
            count += 1
    return count
    
    
def paralleleLinien(n):
    if n == 1:
        return 0
    else:
        return paralleleLinien(n-1) + 4* euler_totient(n-1)



print(umfang(3,3))
print(flaecheninhalt(3,3))