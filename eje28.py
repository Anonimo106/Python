dic={}
indice="nombre"
valor="Jairo"
dic[indice]=valor
# dic.setdefault(indice,valor)
print (dic)
menu=True
while menu:
    op=int(input("Elija una opcion\n1.-Agregar\n2.-Salir\n"))
    if op==1:
        indice=input("Ingrese el indice: ")
        valor=input("Ingrese el valor: ")
        dic[indice]=valor
        print(dic)
    elif op==2:
        menu=False
    else:
        print("Ingrese una opcion valida")