sexo='m'
edad=59
cotizciones=800
aniosServ=26

if aniosServ>=25 and cotizciones>=750:
    if (sexo=='m' and edad>=60) or (sexo=='f' and edad>=55):
        print("Usted aplica para ser jubilado")
    else:
        print("Ustes no apllica para ser jubilado")
else:
        print("Ustes no apllica para ser jubilado")