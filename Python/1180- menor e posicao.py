posicao = []
n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    posicao.append(a[i])
    if posicao[i] == min(posicao):
        menor = i
print("Menor valor: {}".format(min(posicao)))
print('Posicao: {}'.format(menor))

