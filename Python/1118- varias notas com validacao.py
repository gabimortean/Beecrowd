while True:
    quant = 0
    soma = 0
    while quant < 2:
        n1 = float(input())
        if 0 <= n1 <= 10:
            quant += 1
            soma += n1
        else:
            print('nota invalida')
    media = soma / 2.00
    print('media = {:.2f}'.format(media))

    resp = 0

    while True:
        print('novo calculo (1-sim 2-nao)')
        resp = int(input())
        if resp == 1 or resp == 2:
            break
    if resp == 2:
        break

