t = int(input())
for y in range(t):
    n = int(input())
    posicao = [0, 1]
    i = 0
    for (i) in range(n+1):
        posicao.append(int(posicao[-1] + posicao[-2]))
    print('Fib({}) = {}'.format(n,posicao[i]))
