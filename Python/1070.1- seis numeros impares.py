x = int(input())
y = int(input())

if x > y:
    maior = x
    menor = y
else:
    maior = y
    menor = y

menor += 1
soma = 0

while (menor < maior):
    if (menor % 2 != 0):
        soma += menor
    menor += 1
print(soma)
