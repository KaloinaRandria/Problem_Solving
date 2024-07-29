# P6:
# Un nombre premier est appelé un nombre premier circulaire si toutes rotations possibles de ces chiffres sont premiers.
#  	Ex: 197 est un premier circulaire car 719 et 971 est premier.
# Trouver tout les nombres premiers inférieurs a 1000000.
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

def rotateNumber(nombre):
    valiny = []
    n = str(nombre)
    for i in range(len(n)):
        rotation = n[i:] + n[:i]
        valiny.append(int(rotation))
    return valiny

def estTableauNbPremier(rotaNumber):
    for i in rotaNumber:
        if not estPremier(i):
            return False
    return True

def generateFirstCircular(nombre):
    valiny = []
    seen = set() #utiliser un ensemble pour eviter les doublons
    for i in range(2,nombre):
        if i not in seen:
            rotations = rotateNumber(i)
            if estTableauNbPremier(rotations):
                valiny.append(i)
                seen.update(rotations)
                print(i)
    return valiny

generateFirstCircular(1000000)