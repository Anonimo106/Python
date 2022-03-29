lista = [80,34,80,23,70]
maximo=lista[0]
suma=0
for i in range (len(lista)):
    for j in range (i+1,len(lista)):
          
        suma=lista[i]+lista[j]
        if suma<=150:
            print("Peso de:",lista[i],"+",lista[j],"=",suma)
            if  maximo<suma:
                maximo=suma
print("el peso maximo posible es:",maximo)

    
