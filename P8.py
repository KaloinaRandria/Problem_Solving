# P8:
# Les nombres triangulaires, pentagonales et hexagonales sont générés par les formules suivantes:
# 	 Triangulaire: Tn=n(n+1)/2, 1,2,3,6,10,...
# 	 pentagonal: Pn=n(3n-1)/2 , 1,5,12,22,35...
# 	 hexagonal: Hn=n(2n-1), 1,6,15,28,45,…
# On remarque qu'on a: T285=P165=H143=40755
# Trouver le prochain nombre qui est a la fois triangulaire, pentagonal et hexagonal.

def triangulaire(n):
    return n*(n+1)//2

def pentagonal(n):
    return n*(3*n-1)//2

def hexagonal(n):
    return n*(2*n-1)

def findNextTPH(start):
    n=start
    while True:
        n+=1
        tri = triangulaire(n)
        if pentagonal(tri) and hexagonal(tri):
            return tri

# print(findNextTPH(285))
print(pentagonal(165))    