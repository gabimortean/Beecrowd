operacao = input()
m = []
for i in range(12):
    m.append([])
    for j in range(12):
        x = float(input())
        m[i].append(x)

# ADP - elementos acima da diagonal principal: i < j
ADP = []
cont = 0
for i in range(12):
    for j in range(12):
        if i < j:
            ADP.append(m[i][j])
            cont += 1
if operacao == 'S':
    print(sum(ADP))

elif operacao == 'M':
    print('{:.1f}'.format(sum(ADP) / cont))




