d = input().split()
di = int(d[1])
h = input().split()
hi = int(h[0])
mi = int(h[2])
si = int(h[4])

d1 = input().split()
df = int(d1[1])
h2 = input().split()
hf = int(h2[0])
mf = int(h2[2])
sf = int(h2[4])

dia = df - di
hora = hf - hi
minu = mf - mi
seg = sf - si

if hi > hf:
    i = hi - hf
    dia = df - di - 1
    hora = 24 - i

if mi > mf:
    i = mi - mf
    hora = hf - hi - 1
    minu = 60 - i

if si > sf:
    i = si - sf
    minu = mf - mi - 1
    seg = 60 - i

if(dia <= 0):
    dia = 0

print('{} dia(s)'.format(dia))
print('{} horas(s)'.format(hora))
print('{} minuto(s)'.format(minu))
print('{} seg(s)'.format(seg))


