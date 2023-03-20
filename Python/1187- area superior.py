operacao = input()
m = []
for i in range(12):
    m.append([])
    for j in range(12):
        x = float(input())
        m[i].append(x)

# AS - elementos area superior: interseccao acimaDS and acimaDP
AS = []
cont = 0
for i in range(12):
    for j in range(12):
        if ((i < j) and (0 <= (i + j) <= 10)):
            AS.append(m[i][j])
            cont += 1
if operacao == 'S':
    print('{:.1f}'.format(sum(AS)))

elif operacao == 'M':
    print('{:.1f}'.format(sum(AS) / cont))