# P5:
# On remarque que 145=1!+4!+5!=1+24+120.
# Trouver tout les entiers naturels qui sont égaux a la somme des factoriels de leurs chiffres.
import math

def separateNumber(nombre):
    return [int(chiffre) for chiffre in str(nombre)]

def equalsFactoriel(limit):
    valiny = []
    for n in range(10,limit):
        num = separateNumber(n)
        temp = sum(math.factorial(chiffre) for chiffre in num)
        if temp == n:
            valiny.append(n)
    return valiny

print(equalsFactoriel(1000000))

    