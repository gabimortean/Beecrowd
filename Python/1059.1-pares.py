y = 0
sum = 0.0

for i in range(1, 7):
    n = float(input())
    if n > 0:
        y += 1
        sum += n

print('{} valores positivos'.format(y))
print("%0.1f" % (sum / y))
