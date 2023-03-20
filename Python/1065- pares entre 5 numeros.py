cont = 0

for i in range(1, 6):
    n = int(input())
    if n % 2 == 0:
        cont+=1
print('{} valores pares'.format(cont))
