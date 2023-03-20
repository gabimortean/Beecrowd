n = int(input())

for i in range(n):
    a = [int(num) for num in input().split(" ")]
    x = min(a)
    y = max(a)
    soma = 0

    for num in range(x + 1, y):
        if num % 2 != 0:
            soma += num
    print(soma)

