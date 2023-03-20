operacao = input()
m = []
for i in range(12):
    m.append([])
    for j in range(12):
        x = float(input())
        m[i].append(x)

# ADP - elementos abaico da diagonal secundaria: 12 <= (i + j) <= 22
ADS = []
cont = 0
for i in range(12):
    for j in range(12):
        if 12 <= (i + j) <= 22:
            ADS.append(m[i][j])
            cont += 1
if operacao == 'S':
    print(sum(ADS))

elif operacao == 'M':
    print('{:.1f}'.format(sum(ADS) / cont))