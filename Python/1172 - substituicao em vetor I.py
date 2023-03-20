posicao = []
for i in range(10):
    x = int(input())
    if x <= 0:
        x = 1
    posicao.insert(i,x)

    print('X[{}] = {}'.format(i,posicao[i]))
