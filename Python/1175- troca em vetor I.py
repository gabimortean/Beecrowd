posicao=[]
for i in range(20):
    x = int(input())
    posicao.append(x)
a = posicao[::-1]
for j in range(20):
    print('N[{}] = {}'.format(j,a[j]))
