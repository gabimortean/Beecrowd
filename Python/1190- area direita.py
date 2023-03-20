operacao = input()
m = []
for i in range(12):
    m.append([])
    for j in range(12):
        x = float(input())
        m[i].append(x)

# AD - elementos area direita: interseccao acimaDP and abaixoDS
AD = []
cont = 0
for i in range(12):
    for j in range(12):
        if ((i < j) and (12 <= (i + j) <= 22)):
            AD.append(m[i][j])
            cont += 1
if operacao == 'S':
    print('{:.1f}'.format(sum(AD)))

elif operacao == 'M':
    print('{:.1f}'.format(sum(AD) / cont))
