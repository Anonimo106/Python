correctos=int(input("Ingrese el numero de aciertos: "))
errores=int(input("Ingrese el numero de errores: "))
total=correctos +errores
pCorrecto=(100/total)*correctos
pErrores=(100/total)*errores
print("su puntaje final fue: "+str(correctos)+"/"+str(errores))
print("Su porcentaje de aciertos es: %.2f y un porcnetaje de errores de: %.2f"%(pCorrecto,pErrores))