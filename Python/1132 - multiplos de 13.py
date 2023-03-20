x = int(input())
y = int(input())

menor = min(x, y)
maior = max(x, y)

soma = 0

for num in range(menor, maior + 1):
    if num % 13 != 0:
        soma += num
print(soma)

