n = input().split(" ")
a, b = n

if a == '1':
    print('Total: R$ {:.2f}'.format(float(b) * 4.00))

if a == '2':
    print('Total: R$ {:.2f}'.format(float(b) * 4.50))

if a == '3':
    print('Total: R$ {:.2f}'.format(float(b) * 5.00))

if a == '4':
    print('Total: R$ {:.2f}'.format(float(b) * 2.00))

if a == '5':
    print('Total: R$ {:.2f}'.format(float(b) * 1.50))
