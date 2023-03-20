x = int(input())
while True:
    y = int(input())
    if y > x:
        break
soma = x
cont = 1
while(soma < y):
    soma+= cont + x
    cont+=1
print(cont)
