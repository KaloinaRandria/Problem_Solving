# P4:
# Considérons la suite de Fibonnaci (Fn) nE IN
# Fn =1 si n=0 ou n=1
# Fn =Fn-1 + Fn-2 si n>=2
# 	Ex: 1,1,2,3,5,8,13,21,34,55,89,144
# 	F11 est le premier terme de la suite qui contient 3 chiffres.
# Trouver le plus petit n tq Fn est le premier terme contenant 1000 chiffres.
def fibonnaci(nombre):
    if nombre < 1 :
        return nombre
    return abs(fibonnaci(nombre-1) + fibonnaci(nombre-2))

def searchN(count):
    n = 1
    while True:
        fn = fibonnaci(n)
        if count == len(str(fn)):
            return fn
        n += 1

print (searchN(10))

