# P1:
# On sait que 2^15 =327668 et la somme de ces chiffres est 26.
# Trouver la somme des chiffres du nombre 2^1000.

def separateChiffre(nombre):
    chiffres = []
    while nombre > 0:
        chiffres.append(nombre % 10)
        nombre //= 10
    return chiffres

def additionnerChiffres(nombre):
    valiny = 0
    chiffres = separateChiffre(nombre)
    for i in range(len(chiffres)):
        valiny = valiny + chiffres[i]
    return valiny
print(additionnerChiffres(2**1000))

    