s = float(input())

i8 = (s - 2000) * 0.08
i18 = (0.08 * 1000) + ((s - 3000) * 0.18)
i28 = (0.08 * 1000) + (0.18 * 1500) + ((s - 4500) * 0.28)

if 0 <= s <= 2000.00:
    print('Isento')

elif 2000.01 <= s <= 3000.00:
    print('R$ {:.2f}'.format(i8))

elif 3000.01 <= s <= 4500.00:
    print('R$ {:.2f}'.format(i18))

elif s > 4500.00:
    print('R$ {:.2f}'.format(i28))
