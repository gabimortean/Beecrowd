x = int(input())
while True:
    y = int(input())
    if y > x:
        break
cont = soma = 0
while (soma < y):
    soma += x
    cont += 1
    x += 1
print(cont)

