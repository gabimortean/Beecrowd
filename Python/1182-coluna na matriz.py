coluna = int(input())
operacao = input()

m = []
for i in range(12):
    m.append([])

    for j in range(12):
        x = float(input())
        m[i].append(x)

if operacao == 'S':
    soma = 0
    for k in range(12):
        soma = soma + m[k][coluna]
    print(soma)
if operacao == 'M':
    med = 0
    soma = 0
    for k in range(12):
        soma = soma + m[k][coluna]
    med = soma / 12
    print('{:.1f}'.format(med))