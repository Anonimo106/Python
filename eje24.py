def Imprimir(tabla):
    for i in range (len(tabla)):
        print("[",end="")
        for j in range (len(tabla)):
            print("%3s"%tabla[i][j],end="")
        print(" ]")


def LlenarSecuencial(n):
    tabla=[]
    cont=0
    for i in range(n):
        tabla.append([])
        for j in range (n):
            cont+=1
            tabla[i]+=[cont]
    return tabla
tabla=LlenarSecuencial(5)
Imprimir(tabla)