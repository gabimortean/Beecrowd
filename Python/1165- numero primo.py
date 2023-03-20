n = int(input())
for i in range(n):
    x = int(input())
    j = 0
    soma = 0

    for j in range(1, x + 1):
        if x % j == 0:
            soma += 1
        j += 1
    if soma == 2:
        print('{} eh primo'.format(x))
    else:
        print('{} nao eh primo'.format(x))
