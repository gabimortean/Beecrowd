posicao = []
for i in range(100):
    x = float(input())
    posicao.insert(i, x)
    if x <= 10.0:
        print('A[{}] = {}'.format(i, posicao[i]))

