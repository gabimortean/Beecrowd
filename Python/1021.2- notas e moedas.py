N = float(input())

A = N

cem = N / 100
r1 = N % 100

cinq = r1 / 50
r2 = r1 % 50

vinte = r2 / 20
r3 = r2 % 20

dez = r3 / 10
r4 = r3 % 10

cinco = r4 / 5
r5 = r4 % 5

dois = r5 / 2

um = r5 % 2

A = N * 100
B = int(A)
C = B % 100

cinqcent = C / 50
r6 = C % 50

vintecincocent = r6 / 25
r7 = r6 % 25

dezcent = r7 / 10
r8 = r7 % 10

cincocent = r8 / 5

umcent = r8 % 5



print("NOTAS:")
print("{} nota(s) de R$ 100.00".format(int(cem)))
print("{} nota(s) de R$ 50.00".format(int(cinq)))
print("{} nota(s) de R$ 20.00".format(int(vinte)))
print("{} nota(s) de R$ 10.00".format(int(dez)))
print("{} nota(s) de R$ 5.00".format(int(cinco)))
print("{} nota(s) de R$ 2.00".format(int(dois)))
print("MOEDAS:")
print("{} moeda(s) de R$ 1.00".format(int(um)))
print("{} moeda(s) de R$ 0.50".format(int(cinqcent)))
print("{} moeda(s) de R$ 0.25".format(int(vintecincocent)))
print("{} moeda(s) de R$ 0.10".format(int(dezcent)))
print("{} moeda(s) de R$ 0.05".format(int(cincocent)))
print("{} moeda(s) de R$ 0.01".format(int(umcent)))
