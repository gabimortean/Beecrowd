n = int(input())

posicao = [0, 1]

for i in range(n):
    posicao.append(posicao[-1] + posicao[-2])
    if i == n -1:
        print(posicao[i], end='\n')
    else:
        print(posicao[i], end=' ')
