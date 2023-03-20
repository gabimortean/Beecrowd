n = int(input())

cont = 0
cont2 = 0

for i in range(n):
    x = int(input())
    if (10 <= x <= 20):
        cont +=1
    else:
        cont2 +=1

print('%d in' % cont)
print('%d out' % cont2)
