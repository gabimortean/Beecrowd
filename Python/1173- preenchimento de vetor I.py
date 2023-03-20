posicao = []
v = int(input())
for i in range(10):
    posicao.insert(i, v)
    v *= 2

    print('N[{}] = {}'.format(i, posicao[i]))
