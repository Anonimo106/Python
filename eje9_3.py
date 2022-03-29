hora = 23
minuto = 59
segundo = 59
print("La hora es:", hora, ":", minuto, ":", segundo)
if hora <= 23 and minuto == segundo <= 59:
    segundo += 1
    if segundo == 60:
        minuto += 1
        segundo = 0
    if minuto == 60:
        hora += 1
        minuto = 0
    if hora == 24:
        hora = 0
    print("La hora un segundo despues es:", hora, ":", minuto, ":", segundo)
else:
    print("Ingrese una hora valida")
