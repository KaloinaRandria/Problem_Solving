# P2:
# Un triplet de Pythagore est un triplet d'entiers d'entiers naturels (a,b,c) tel que a<b<c et a^2+b^2=c^2.
# Il existe un triplet de Pythagore (a,b,c) tel que a+b+c=1000.

def tripletPythagore(nombre):
    for a in range(1,nombre // 2):
        for b in range(a+1,nombre // 2):
            c = nombre - a - b
            if c > b and a*a + b*b == c*c :
                return [a,b,c]
    return []

print(tripletPythagore(30))