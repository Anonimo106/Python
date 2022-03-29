def Imprimir(dic):
    for indice in dic:
        print("Codigo", indice, "Informacion:", dic[indice])


def AgregarEstudiante(dic, codigo, nombre):
    dic[codigo] = []
    dic[codigo].append(nombre)
    dic[codigo].append([])


def AgregarNotas(dic, codigo, nota):
    dic[codigo][1] += [nota]


def Promedio(lista):
    suma = 0
    for item in lista:
        suma += item
    return suma/len(lista)


def Consulta(codigo):
    if dic == None:
        print("Informacion no encontrada")
    else:
        print(dic.get(codigo))


dic = {}
menu = True

while menu:
    op = int(input(
        "Escoga una opcion\n1.-Agregar estudiante\n2.-agregar notas\n3.-Consultar informacion\n4.-salir\n"))
    if op <= 4:
        if op == 1:
            codigo = input("Agregar un codigo para guardar la informacion: ")
            nombre = input("Agregar un nombre: ")
            AgregarEstudiante(dic, codigo, nombre)
            Imprimir(dic)
        elif op == 2:
            codigo = input("Ingrese el codigo del estudiante: ")
            notas = input("Agregar notas: ")
            AgregarNotas(dic, codigo, notas)
            Imprimir(dic)
        elif op == 3:
            codigo = input("Ingrese el codigo del estudiante: ")
            Consulta(codigo)
        elif op == 4:
            menu = False
    else:
        input("Ingrese una opcion valida")


Imprimir(dic)
AgregarEstudiante(dic, "001", "Kevin")
AgregarNotas(dic, "001", 10)
AgregarNotas(dic, "001", 8)
Imprimir(dic)
print(Promedio(dic["001"][1]))
