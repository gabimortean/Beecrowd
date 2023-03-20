
while True:
    ordem = int(input())
    if ordem == 0:
        break
    else:
        m = []
        for i in range(ordem):
            linha = []
            for j in range(ordem):
                x = i
                if j > x:
                    x = j
                elif (ordem - i + 1) < x:
                    x = ordem - i + 1
                elif (ordem - j + 1) < x:
                    x = ordem - j + 1

                linha.append(x)
            m.append(linha)
        break

for i in range(ordem):
    for j in range(ordem):
        print(m[i][j], end = " ")
    print("")
