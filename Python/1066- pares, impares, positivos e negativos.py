cont = 0
cont2 = 0
cont3 = 0
cont4 = 0

for i in range(1,6):
    n = int(input())
    if n % 2 == 0:
        cont +=1
    if n % 2 != 0:
        cont2 +=1
    if n > 0:
        cont3 +=1
    if n < 0:
        cont4 +=1
print('{} valor(es) par(es)'.format(cont))
print('{} valor(es) impar(es)'.format(cont2))
print('{} valor(es) positivo(s)'.format(cont3))
print('{} valor(es) negativo(s)'.format(cont4))
