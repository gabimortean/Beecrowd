quant = 0
soma = 0
while True:
    if quant == 2:
        break
    n1 = float(input())
    if 0 <= n1 <= 10:
        quant += 1
        soma += n1
    else:
        print('nota invalida')
media = soma / 2.00
print('media = {:.2f}'.format(media))



