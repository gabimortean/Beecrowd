x = list(map(int, input().split()))
i = 1
soma = 0
#enquanto o segundo elemento da lista (i = 1) for <0
while x[i] <= 0:
    if x[i] <= 0:
        i+=1
    if x[i] > 0:
        break

for c in range(x[i]):
    soma += x[0] + c

print(soma)

