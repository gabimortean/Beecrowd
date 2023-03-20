while True:
    a = input().split()
    x, y = (a)

    if int(x) == int(y):
        break
    else:
        if int(x) > int(y):
            print('Decrescente')
        else:
            print('Crescente')
            