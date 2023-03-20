i = 0
j = 0
while True:
    idade = int(input())
    if idade >= 0:
        i += idade
        j += 1

    else:
        print('{:.2f}'.format(i / j))
        break

