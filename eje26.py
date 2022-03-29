from random import randint


def Imprimir(tabla):
    for fila in tabla:
        print("[", end="")
        for columna in fila:
            print("%3s" % columna, end="")
        print(" ]")


def LlenarVacio(n):
    tabla = []
    for i in range(n):
        tabla.append([])
        columnas = randint(1, 10)
        for j in range(columnas):
            tabla[i] += [randint(1, 10)]
    return tabla


tabla = LlenarVacio(5)
Imprimir(tabla)
