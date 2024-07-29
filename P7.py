# P7:
#  Si p désigne le périmètre d'un triangle rectangle de cotes a,b et c avec a,b,c C N,
# il existe exactement 3 solutions pour p=120, a savoir: {20,48,52}, {24,45,51},{30,40,50} 	
# Contrainte: {(m'2-n'2), 2mn, (n'2+m'2)}
# Pour quelle valeur de p<=1000 a-t-on le plus possible de solution?

def pgcd(a,b):
    while b:
        a, b = b, a % b
    return a
def generatePythagoreTriplets(limit):
    count = {}
    for m in range(2,int((limit/2)**0.5) + 1):
        for n in range(1,m):
            if (m-n) % 2 == 1 and pgcd(m,n) ==  1:
                a = m*m - n*n
                b = 2*m*n
                c = m*m + n*n
                p = a + b + c
                while p <= limit:
                    if p in count:
                        count[p] += 1
                    else:
                        count[p] = 1
                    p += a+b+c
    return count

def findMaxSolution(limit):
    count = generatePythagoreTriplets(limit)
    max_p = max(count , key=count.get)
    return max_p,count[max_p]

print(findMaxSolution(1000))