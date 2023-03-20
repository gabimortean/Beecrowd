s1 = 0
s2 = 0
empate = 0
quant = 0

while True:
    g1, g2 = input().split()
    g1 = int(g1)
    g2 = int(g2)
    if (g1 > g2):
        s1 += 1
    elif (g1 < g2):
        s2 += 1
    else:
        empate += 1

    quant += 1
    print("Novo grenal (1-sim 2-nao)")
    n = int(input())
    if (n == 1):
        continue
    elif (n == 2):
        break
print("{} grenais".format(quant))
print("Inter:{}".format(s1))
print("Gremio:{}".format(s2))
print("Empates:{}".format(empate))
if (s1 > s2):
    print("Inter venceu mais")
if (s1 < s2):
    print("Gremio venceu mais")
if (s2 == s1):
    print("Nao houve vencedor")
