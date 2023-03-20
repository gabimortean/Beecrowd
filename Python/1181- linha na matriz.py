l = int(input())
operacao = input()

matriz = []
for i in range(12):
    matriz.append([])

    for j in range(12):
        x = float(input())
        matriz[i].append(x)

if operacao == 'S':
    soma = 0
    for k in matriz[l]:
        soma += k
    print(soma)
if operacao == 'M':
    med = 0
    soma = 0
    for k in matriz[l]:
        soma += k
    med= soma/12
    print(med)