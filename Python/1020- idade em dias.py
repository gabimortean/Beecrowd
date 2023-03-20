N = int(input())

ano = int(N // 365)
N = N - ano * 365

mes = int(N // 30)
N = N - mes * 30

dia = N

print('{} ano(s)'.format(ano))
print('{} mes(es)'.format(mes))
print('{} dia(s)'.format(dia))
