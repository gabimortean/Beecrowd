x = float(input())
posicao = []
i = 0
for i in range(100):
    posicao.append(x)
    x /= 2
    print('N[{}] = {:.4f}'.format(i, posicao[i]))
