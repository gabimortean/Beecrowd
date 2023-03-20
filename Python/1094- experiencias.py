n = int(input())
cont, c, r, s = 0, 0, 0, 0

for i in range(n):
    quantia, tipo = input().split()
    cont += int(quantia)
    if tipo == 'C':
        c += int(quantia)
    elif tipo == 'R':
        r += int(quantia)
    elif tipo == 'S':
        s += int(quantia)

print('Total: {} cobaias'.format(cont))
print('Total de coelhos: {}'.format(c))
print('Total de ratos: {}'.format(r))
print('Total de sapos: {}'.format(s))
print('Percentual de coelhos: {:.2f} %'.format(float(c / cont * 100)))
print('Percentual de ratos: {:.2f} %'.format(float(r / cont * 100)))
print('Percentual de sapos: {:.2f} %'.format(float(s / cont * 100)))

