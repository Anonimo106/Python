

from random import randint

zonaUsiario=int(input("¿En que zona desea disparar?: "))
zonaPortero=randint(1,6)

print("La zona cubierta por el portero es:",zonaPortero)

if zonaUsiario==zonaPortero:
    print("No ha sido gol")
else:
    print("Gooooooooooooool")