lista=["hola","gato","perro","gato","palabra","hola"]
print (lista)
for i in range((len(lista)-1),-1,-1):
    
    if  lista[i] in lista[:i]:
        del(lista[i])

print (lista)