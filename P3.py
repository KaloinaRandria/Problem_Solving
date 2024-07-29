# P3:
# Trouver le 500001eme nombre premier.
def estPremier(nombre):
    if nombre <= 1:
        return False
    if nombre <= 3:
        return True
    if nombre % 2 == 0 or nombre % 3 == 0:
        return False
    i = 5
    while i*i <= nombre:
        if nombre % i == 0 or nombre % (i+2) == 0:
            return False
        i += 6
    return True

def searchNiemePremier(nieme):
    if nieme < 1:
        raise ValueError("nieme doit etre un entier positif")
    count = 0
    nombre = 2
    while True:
        if estPremier(nombre):
            count +=1
            if count == nieme:
                return nombre
        nombre +=1

print (searchNiemePremier(500001))