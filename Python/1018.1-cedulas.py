N = int(input())
valor = N
notas = [100, 50, 20, 10, 5, 2, 1]
cont = 0
print(valor)
for i in range(len(notas)):
    cont = N // notas[i]
    N %= notas[i]
    print('{} nota(s) de R$ {},00'.format(cont, notas[i]))
