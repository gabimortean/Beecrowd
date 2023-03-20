n = int(input())

for i in range(n):
    x = int(input())
    j = 0
    soma = 0

    for j in range(1, x):
        if x % j == 0:
            soma+= j
        j += 1
    if soma == x:
        print('{} eh perfeito'.format(x))
    else:
        print('{} nao eh perfeito'.format(x))







