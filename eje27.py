def Imprimir(tabla):
    for fila in tabla:
        print("[", end="")
        for columna in fila:
            print("%3s" % columna, end="")
        print(" ]")


def ComprobarGandor(tabla, simbolo):
    win = False
    win2 = True
    win3 = True
    win4 = True
    for i in range(len(tabla)):
        if tabla[i].count(simbolo) == 3:
            win = True
        win2 = True
        for j in range(len(tabla)):
            win2 = tabla[j][i] == simbolo and win2
        if win2 == True:
            break
        win3 = tabla[i][i] == simbolo and win3
        win4 = tabla[i][(len(tabla)-i-1)] == simbolo and win4
    if win or win2 or win3 or win4:
        return True
    else:
        return False


tabla = [["x", " ", "x"],
         ["x", " ", " "],
         ["x", " ", " "]]
print(ComprobarGandor(tabla, "x"))
