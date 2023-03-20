def ordem(lista):
    a, b, c = lista
    return (a, b, c)


def codifica(tamanho):
    if tamanho == 'P':
        tamanho = -3
    if tamanho == 'M':
        tamanho = -2
    if tamanho == 'G':
        tamanho = -1
    return tamanho


def descodifica(tamanho):
    if tamanho == -3:
        tamanho = 'P'
    if tamanho == -2:
        tamanho = 'M'
    if tamanho == -1:
        tamanho = 'G'
    return tamanho


first = False

while True:

    n = int(input())
    if n == 0: break
    suporte = []
    ficha = []

    for i in range(n):
        nome = input()
        cor, tamanho = input().split()
        tamanho = codifica(tamanho)
        ficha.append([cor, tamanho, nome])

    ficha.sort(key=ordem)

    for el in ficha:
        el[1] = descodifica(el[1])

    if first:
        print()

    for aluno in ficha:
        print('{} {} {}'.format(aluno[0], aluno[1], aluno[2]))

    '''
        for elemento in ficha:
        print(*elemento,sep = ' ')


    '''
    first = True
    