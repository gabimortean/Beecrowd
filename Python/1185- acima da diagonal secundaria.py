operacao = input()
m = []
for i in range(12):
    m.append([])
    for j in range(12):
        x = float(input())
        m[i].append(x)

# ADP - elementos acima da diagonal secundaria: 0 <= (i + j) <= 10
ADS = []
cont = 0
for i in range(12):
    for j in range(12):
        if 0 <= (i + j) <= 10:
            ADS.append(m[i][j])
            cont += 1
if operacao == 'S':
    print(sum(ADS))

elif operacao == 'M':
    print('{:.1f}'.format(sum(ADS) / cont))