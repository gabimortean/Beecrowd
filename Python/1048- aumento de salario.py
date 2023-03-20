s = float(input())
if s <= 400.00:
    novosal = s * 1.15
    reajus = novosal - s
    percent = 15
if 400.01 <= s <= 800.00:
    novosal = s * 1.12
    reajus = novosal - s
    percent = 12
if 800.01 <= s <= 1200.00:
    novosal = s * 1.10
    reajus = novosal - s
    percent = 10
if 1200.01 <= s <= 2000.00:
    novosal = s * 1.07
    reajus = novosal - s
    percent = 7
if s > 2000.00:
    novosal = s * 1.04
    reajus = novosal - s
    percent = 4
print('Novo salario: {:.2f}'.format(novosal))
print('Reajuste ganho: {:.2f}'.format(reajus))
print('Em percentual: {} %'.format(percent))


