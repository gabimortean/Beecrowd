operacao = input()
m = []
for i in range(12):
    m.append([])
    for j in range(12):
        x = float(input())
        m[i].append(x)

# AI - elementos area inferior: interseccao abaixoDS and abaixoDP
AI = []
cont = 0
for i in range(12):
    for j in range(12):
        if ((i > j) and (12 <= (i + j) <= 22)):
            AI.append(m[i][j])
            cont += 1
if operacao == 'S':
    print('{:.1f}'.format(sum(AI)))

elif operacao == 'M':
    print('{:.1f}'.format(sum(AI) / cont))
