# P4:
# Considérons la suite de Fibonnaci (Fn) nE IN
# Fn =1 si n=0 ou n=1
# Fn =Fn-1 + Fn-2 si n>=2
# 	Ex: 1,1,2,3,5,8,13,21,34,55,89,144
# 	F11 est le premier terme de la suite qui contient 3 chiffres.
# Trouver le plus petit n tq Fn est le premier terme contenant 1000 chiffres.
def fibonnaciRecursive(nombre):
    if nombre < 1 :
        return nombre
    return abs(fibonnaciRecursive(nombre-1) + fibonnaciRecursive(nombre-2))

def fibonacciIterative(n):
    """Retourne le n-ième nombre de Fibonacci de manière itérative."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def searchN(count):
    n = 1
    while True:
        fn = fibonacciIterative(n)
        if count == len(str(fn)):
            return fn
        n += 1

print (searchN(1000))

