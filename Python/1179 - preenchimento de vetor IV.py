par = []
impar = []
p = 0
i = 0
cont = 0

for w in range(15):
    x = int(input())
    if x % 2 == 0:
        par.append(x)
        p+=1
    else:
        impar.append(x)
        i+=1

    if p > 4:
        for c in range(5):
            print('par[{}] = {}'.format(c, par[c]))
        par = []
        p = 0
    if i > 4:
        for c in range(0, 5):
            print('impar[{}] = {}'.format(c, impar[c]))
        impar = []
        i = 0
    cont += 1

if i > 0:
    for j in range(i):
        print('impar[{}] = {}'.format(j,impar[j]))
if p > 0:
    for h in range(p):
        print('par[{}] = {}'.format(h,par[h]))
        