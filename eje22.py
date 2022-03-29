from random import randint
def LlenarSec(n):
    lista=[]
    for i in range(1,n+1):
        lista+=[i]
        return lista

def LlenarAle(n):
    lista=[]
    num=randint(1,n)
    lista+=[num]
    for i in range (n-1):
        while num in lista:
            num=randint(1,n)
        lista+=[num]
    return lista

listaA=LlenarSec(10)
listaB=LlenarAle(10)

for i in range (len(listaA)):
    print("La persona",listaA[i],"es pareja",listaB[i])
