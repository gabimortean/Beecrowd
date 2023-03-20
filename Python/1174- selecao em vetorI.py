posicao = []
for i in range(100):
    x = float(input())
    posicao.append(x)
    if x <= 10.0:
        print('A[{}] = {}'.format(i,x))
