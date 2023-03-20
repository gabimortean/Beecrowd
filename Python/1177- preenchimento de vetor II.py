t = int(input())
posicao = []
for i in range(1000):
    j = 0
    for w in range(t):
        posicao.append(j)
        j +=1
    print('N[{}] = {}'.format(i, posicao[i]))
