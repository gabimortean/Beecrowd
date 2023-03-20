N = float(input())


cem = N // 100
N = float(N - cem * 100)

cinq = N // 50
N = float(N - cinq * 50)

vinte = N // 20
N = float(N - vinte * 20)

dez = N // 10
N = float(N - dez * 10)

cinco = N // 5
N = float(N - cinco * 5)

dois = N // 2
N = float(N - dois * 2)

um = N // 1
N = float(N - um)

cinqcent = float(N // 0.50)
N = float(N - cinqcent * 0.50)

vintecincocent = float(N // 0.25)
N = float(N - vintecincocent * 0.25)

dezcent = float(N // 0.10)
N = float(N - dezcent * 0.10)

cincocent = float(N // 0.05)
N = float(N - cincocent * 0.05)

umcent = float(N // 0.01)


print('NOTAS:')
print('%d nota(s) de R$ 100.00' % cem)
print('%d nota(s) de R$ 50.00' % cinq)
print('%d nota(s) de R$ 25.00' % vinte)
print('%d nota(s) de R$ 10.00' % dez)
print('%d nota(s) de R$ 5.00' % cinco)
print('%d nota(s) de R$ 2.00' % dois)

print('MOEDAS:')
print('%d moeda(s) de R$ 1.00' % um)
print('%d moeda(s) de R$ 0.50' % cinqcent)
print('%d moeda(s) de R$ 0.25' % vintecincocent)
print('%d moeda(s) de R$ 0.10' % dezcent)
print('%d moeda(s) de R$ 0.05' % cincocent)
print('%d moeda(s) de R$ 0.01' % umcent)
