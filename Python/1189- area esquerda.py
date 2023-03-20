operacao = input()
m = []
for i in range(12):
    m.append([])
    for j in range(12):
        x = float(input())
        m[i].append(x)

# AE - elementos area esquerda: interseccao abaixoDP and acimaDS
AE = []
cont = 0
for i in range(12):
    for j in range(12):
        if ((i > j) and (0 <= (i + j) <= 10)):
            AE.append(m[i][j])
            cont += 1
if operacao == 'S':
    print('{:.1f}'.format(sum(AE)))

elif operacao == 'M':
    print('{:.1f}'.format(sum(AE) / cont))
