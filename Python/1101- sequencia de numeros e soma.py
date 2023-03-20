while True:

    m, n = list(map(int, input().split()))

    if m <= 0 or n <= 0:
        break
    else:
        menor = min(m, n)
        maior = max(m, n)

        soma = 0

        for num in range(menor, maior + 1):
            soma += num
            print(num, end=' ')
        print('Sum={}'.format(soma))
