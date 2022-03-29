
def vasos(n,x):
    total=0
    while n>=x:
        reciclados=n//x
        sobra=n%x
        total+=reciclados
        n=reciclados+sobra
        print("N",n,"Reciclados:",reciclados,"sobran",sobra,"total reciclados",total)
    return total

n=10
x=4
print(vasos(10,4))